import os
from dotenv import load_dotenv
from Utilities.random_util import random_string

load_dotenv()

website_link = os.getenv("site_link")

firstname = "Aditya"
lastname = "Bhati"

# Generate a unique email using a random string
email = f"{random_string()}@example.com"
password = os.getenv("password")





