import requests
import os
import pytest

CATTLE_TEST_URL = os.environ.get('CATTLE_TEST_URL', "")
ADMIN_USER = os.environ.get('ADMIN_USER', "admin")
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', "password")

HARVESTER_LOGIN_URL = "/v1-public/auth?action=login"