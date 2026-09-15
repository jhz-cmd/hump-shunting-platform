# -*- coding: utf-8 -*-
import base64, json, io, sys

src = sys.argv[1]
out = sys.argv[2]
msg = sys.argv[3] if len(sys.argv) > 3 else 'update'
sha = sys.argv[4] if len(sys.argv) > 4 else None
data = io.open(src, 'rb').read()
payload = {"message": msg, "content": base64.b64encode(data).decode('ascii'), "branch": "main"}
if sha:
    payload["sha"] = sha
io.open(out, 'w', encoding='utf-8').write(json.dumps(payload, ensure_ascii=False))
print('written', out, len(data), 'bytes', 'sha=' + (sha or 'none'))
