import re
from datetime import datetime

def parse_date_robust(title):
    match = re.search(r'\[\s*(\d{2})[-.](\d{2})[-.](\d{2}|\d{4})\s*\]', title)
    if match:
        d, m, y = match.groups()
        if len(y) == 2:
            y = "20" + y
        try:
            return datetime(int(y), int(m), int(d))
        except ValueError:
            pass
    return None

print(parse_date_robust("[17-01-26] Test"))
print(parse_date_robust("[17.01.26] Test"))
print(parse_date_robust("[ 17-01-2026 ] Test"))
