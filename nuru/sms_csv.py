import os
import africastalking as at
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("03fa1168ce6c4b6c4531edd04c9352a15ec17f92271ca847beea8fa910808a1e")
username = os.getenv("Nuru")
at.initialize(username, api_key)
sms = at.SMS


