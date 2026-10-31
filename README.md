# Flask starter

A minimal [Flask](https://flask.palletsprojects.com) app served by gunicorn.

## Run it locally

```sh
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then open http://localhost:8080. `GET /health` answers `ok` for health checks.

## Deploying

| Step | Command |
| --- | --- |
| Build | pip install -r requirements.txt |
| Start | gunicorn --bind 0.0.0.0:$PORT main:app |

## Environment variables

| Variable | Meaning |
| --- | --- |
| `PORT` | Port to listen on. Default: 8080. |

## Notes

Dependencies are pinned in `requirements.txt`, generated from `requirements.in` with `uv pip compile requirements.in -o requirements.txt`.

## License

MIT
