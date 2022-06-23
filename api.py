from flask import Flask
import threading

import asyncio
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def demo():
    return "Hello "


if __name__ == "__main__":
    app.run (debug = True)   
    