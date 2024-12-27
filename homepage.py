from flask import Flask, request, jsonify, render_template
import requests
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

HOMESERVER = os.getenv("HOMESERVER")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

join_requests = {}

# route for users to request to create a new account
@app.route("/request-token", methods=["POST"])
def request_join():
    data = request.json
    username = data.get("username")
    usertype = data.get("usertype")