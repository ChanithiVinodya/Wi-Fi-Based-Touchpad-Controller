#!/usr/bin/env python3
"""
touchpad_server.py
WebSocket server for remote phone touchpad control.
"""

import asyncio
import json
import logging
import os
import signal
from typing import Any

import pyautogui
import websockets

print("Modules are working 🥳")

# ------- Configuration -------
HOST = "0.0.0.0"
PORT = 9000
DEFAULT_SENSITIVITY = 1.0
# -----------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


class ClientState:
    def __init__(self):
        self.sensitivity = DEFAULT_SENSITIVITY
        self.dragging = False


async def handle_message(state: ClientState, msg: str):
    """
    Parse & handle a JSON message from client.
    """
    try:
        obj = json.loads(msg)
    except json.JSONDecodeError:
        logging.warning("Invalid JSON: %s", msg)
        return

    t = obj.get("type")

    if t == "move":
        dx = float(obj.get("dx", 0)) * state.sensitivity
        dy = float(obj.get("dy", 0)) * state.sensitivity
        pyautogui.moveRel(dx, dy, _pause=False)

    elif t == "click":
        btn = obj.get("btn", "left")
        pyautogui.click(button=btn)
        logging.info("Click: %s", btn)

    elif t == "mousedown":
        btn = obj.get("btn", "left")
        pyautogui.mouseDown(button=btn)
        state.dragging = True

    elif t == "mouseup":
        btn = obj.get("btn", "left")
        pyautogui.mouseUp(button=btn)
        state.dragging = False

    elif t == "scroll":
        pyautogui.scroll(int(obj.get("dy", 0)))

    elif t == "set_sensitivity":
        new_s = float(obj.get("s", DEFAULT_SENSITIVITY))
        state.sensitivity = max(0.1, min(10.0, new_s))
        logging.info("Sensitivity: %.2f", state.sensitivity)

    elif t == "ping":
        logging.debug("Ping received")

    else:
        logging.warning("Unknown type %s | %s", t, obj)


async def handler(ws: websockets.WebSocketServerProtocol):
    ip = ws.remote_address[0] if ws.remote_address else "unknown"
    logging.info("Client connected: %s", ip)

    state = ClientState()

    try:
        async for message in ws:
            asyncio.create_task(handle_message(state, message))

    except websockets.ConnectionClosed:
        logging.info("Client disconnected: %s", ip)

    finally:
        if state.dragging:
            try:
                pyautogui.mouseUp()
            except:
                pass
        logging.info("Cleanup: %s", ip)


async def main():
    server = await websockets.serve(handler, HOST, PORT)
    logging.info("Server running at ws://%s:%d", HOST, PORT)

    loop = asyncio.get_running_loop()
    stop = loop.create_future()

    def _stop_signal(*_):
        if not stop.done():
            stop.set_result(True)

    if os.name != 'nt':
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, _stop_signal)

    await stop
    server.close()
    await server.wait_closed()
    logging.info("Server shutdown")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped manually")
