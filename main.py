import websocket
import json

def on_message(ws, message):
    msg = json.loads(message)
    if msg.get('event') == 'gold-rate-event':
        data = json.loads(msg['data'])
        buying_rate = data['buying_rate']
        selling_rate = data['selling_rate']
        waktu = data['created_at']
        print(f"Waktu: {waktu} | Harga Beli: {buying_rate} | Harga Jual: {selling_rate}")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connection opened")
    subscribe_data = {
        "event": "pusher:subscribe",
        "data": {
            "channel": "gold-rate"
        }
    }
    ws.send(json.dumps(subscribe_data))

if __name__ == "__main__":
    ws_url = "wss://ws-ap1.pusher.com/app/52e99bd2c3c42e577e13?protocol=7&client=js&version=7.0.3&flash=false"
    ws = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
