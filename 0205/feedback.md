# FastAPI
## DI (Dependency Injection)
FastAPI에서 Depends 모듈을 사용하여 DI를 할 수 있음.
```py
@router.post("/signin", status_code=200)
def signin(user: User = Depends(validate_user),
           session: Session = Depends(get_db_session)) -> AuthResponse:
```
신기한 점은 default parameter로 작성해두면 된다는 점인데, 처음에는 이해가 안됐었음.
signin에 인자를 넘겨주는 순간 기본 생성자는 의미가 없어질텐데 어떻게 의존성 주입이 되는가 궁금하여 찾아봤음.

힌트는 *fastapi/dependencies/utils.py*에 있음.
최상단에 ```import inspect```가 적혀있는데
이 내장 모듈이 바로 Java의 Reflection과 유사한 역할을 해서 동적으로 코드 조작이 가능하게 됨.
# DB
## DB Transaction
데이터 무결성을 보장하기 위해여 필요함.
DB에 Write를 할 때 꼭 필요함
## sqlmodel 모듈
### commit(), refresh()
```py
@router.post("/", status_code=201)
def create_post(post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session)) -> PostResponse:
    post.created_at = int(time.time())
    session.add(post)
    session.commit()
    session.refresh(post)
    return PostResponse(posts=[post], err_msg=None)
```
commit 함수의 설명을 읽어보면 다음과 같음.
>    When the COMMIT operation is complete, all objects are fully :term:`expired`, erasing their internal contents, which will be automatically re-loaded when the objects are next accessed.

즉, session에 post 변수를 add한 후에 commit()을 하면 post 변수의 값들이 모두 지워진다는 점인데 초심자는 주의해야할 필요가 있을 것 같음.
refresh(post)는 commit으로 사라진 데이터들을 다시 로드해줌.

### add()
```py
@router.put("/{post_id}", status_code=200)
def update_post(post_id: int, 
                post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session)) -> PostResponse:
    old_post = session.get(Post, post_id)
    if not old_post:
        raise HTTPException(status_code=404, detail="Post not found")
    postData = post.model_dump(exclude_unset=True)
    old_post.sqlmodel_update(postData)
    session.add(old_post)
    session.commit()
    session.refresh(old_post)
    return PostResponse(posts=[old_post], err_msg=None)
```
update하는 함수인데 session.add(old_post)가 들어가있음.
기존의 old_post가 있는데 add를 하게 되면 old_post가 또 추가가 되는게 아닌가 의문이 들지만
session의 