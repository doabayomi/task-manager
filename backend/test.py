import auth
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('DEV_ENVIRONMENT'))
print(auth.test)
