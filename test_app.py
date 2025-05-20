from flask import Response
from app import app

def test_home():
  client = app_test_client()
  response = client.get('/')
  assert response.status_code == 200
  assert b"Hello DevOps!" in" response.data
  