#!/bin/bash
# start app

cd "$( dirname "$0" )"

uv run fastapi dev src/app.py \
  > out.log \
  2> err.log
