#!/bin/bash

. /app/venv/bin/activate
exec uvicorn app.main:app