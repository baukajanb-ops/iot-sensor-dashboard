import paho.mqtt.client as mqtt
import psycopg2
import json

BROKER = "localhost"
TOPIC = "iot/sensor/env"

conn = psycopg2.connect(
    dbname="iot_data",
    user="postgres",
    password="postgre",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    cursor.execute("""
        INSERT INTO sensor_data (timestamp, temperature, humidity)
        VALUES (%s, %s, %s)
    """, (data["timestamp"], data["temperature"], data["humidity"]))

    conn.commit()
    print("Saved:", data)

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
client.on_message = on_message

client.loop_forever()
