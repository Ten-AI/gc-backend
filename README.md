# Garbage Classification Backend

## Quick Start

```shell script
pip3 install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000

```

Post `http://127.0.0.1:8000/img/` with `img` body and it will return

```json
{
    "name": "smile.jpg",
    "size": 251
}
```