# fastapi
Simple fast API implementation with `?key=value` queries
```bash
$ sudo pip3 install fastapi
$ pip install uvicorn[standard]
$ uvicorn main:app --reload
```
check for
* Full JSON: http://127.0.0.1:8000/
* Filtered item: http://127.0.0.1:8000/?item_id=6
* Filtered item: http://127.0.0.1:8000/?item_id=6&value=1

