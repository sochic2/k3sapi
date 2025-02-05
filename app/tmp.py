tmp_dockerfile = """
FROM python:3.10-slim

RUN echo "Asia/Seoul" > /etc/timezone

RUN git clone https://github.com/sochic2/fast_api.git

RUN pip install --no-cache-dir -r requirements.txt

#RUN alembic init migrations
#
#RUN mv ./tmp/alembic.ini ./alembic.ini
#
#RUN mv ./tmp/env.py ./migrations/env.py
#
#RUN alembic revision --autogenerate
#
#RUN alembic upgrade head

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
"""