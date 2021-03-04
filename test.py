from dotenv import load_dotenv
import os
from os.path import join,dirname
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
TOKEN_KEY = os.environ.get("TOKEN")
print(TOKEN_KEY)

print("Hello Bruno")
print("Amaral")