max_len = 4000

async def split(data):
    if len(data) < max_len:
        return [data]
    
    parts = []
    while data:
        if len(data) < max_len:
            parts.append(data)
            break
        cut = data.rfind('\n', 0, max_len)
        if cut == -1:
            cut = data.rfind(' ', 0, max_len)
        if cut == -1:
            cut = max_len
        parts.append(data[:cut].strip())
        data = data[cut:].strip()
    return parts
