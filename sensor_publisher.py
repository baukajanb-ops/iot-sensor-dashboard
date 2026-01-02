import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

BROKER = "localhost"        # MQTT брокер
TOPIC = "iot/sensor/env"    # Топик для публикации

# Создаём MQTT клиент
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    # Генерируем случайные данные температуры и влажности
    data = {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2)
    }

    # Отправляем данные в MQTT брокер
    client.publish(TOPIC, json.dumps(data))
    print("Published:", data)

    # Ждём 5 секунд
    time.sleep(5)
