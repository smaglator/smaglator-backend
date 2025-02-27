from app.services.mqtt import send_message, start_connection


class MQTTController:
    def send_message(msg: str, topic: str):
        client = start_connection()
        client.loop_start()
        send_message(client=client, message=msg, topic=topic)
        client.loop_stop()
