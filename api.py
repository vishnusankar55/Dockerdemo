from flask import Flask
import threading

import asyncio
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def demo():
    return "Hello "
@app.route("/test", methods=["GET"])
def index():
    print(f"Inside flask function: {threading.current_thread().name}")
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(hello())
    return jsonify({"result": result})

async def hello():
    await asyncio.sleep(5)
    return 1       


if __name__ == "__main__":
    app.run (debug = True)   
