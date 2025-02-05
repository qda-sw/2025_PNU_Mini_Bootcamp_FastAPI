import re
from dataclasses import dataclass
@dataclass
class URI:
    method:str
    request:str
def parseRequest(request:str)->URI | None:
    if not request:
        return None
    
    match = re.match(r'\b(GET|POST|DELETE|PUT|PATCH)\b\s+(.*?)\s+HTTP/1.1', request)
    if not match:
        return None
    uri = URI(match.group(1), match.group(2))
    return uri