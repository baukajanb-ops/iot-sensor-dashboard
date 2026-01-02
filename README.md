# iot-sensor-dashboard
IoT Sensor Data Collection and Visualization using MQTT, PostgreSQL, and Grafana. Simulated temperature and humidity sensor data is stored and visualized in real time.
---

## Description
The system includes:

- **Publisher**: Python script simulating sensor data (temperature & humidity) and sending it to an MQTT broker every 5 seconds.
- **Subscriber**: Python script subscribing to the MQTT topic and storing messages in PostgreSQL.
- **Visualization**: Grafana dashboard connected to PostgreSQL displaying live temperature and humidity graphs.

---

## Setup
1. Install Python 3.13
2. Install dependencies:
3. Start Mosquitto broker
4. Run subscriber:
5. Run publisher:
6. Open Grafana at http://localhost:3000, configure PostgreSQL data source, and view dashboard.

## Project Structure
iot-sensor-dashboard/
├─ mqtt_subscriber_pg.py   # Subscriber script, writes MQTT data to PostgreSQL
├─ sensor_publisher.py     # Publisher script, simulates sensor data
├─ README.md               # Project explanation and instructions
├─ requirements.txt        # Python dependencies
├─ screenshots/
│   ├─ subscriber.png      # Example output of subscriber console
│   ├─ postgresql.png      # Example of PostgreSQL table content
│   └─ grafana_dashboard.png # Screenshot of Grafana dashboard

## Dependencies
- Python 3.13
- paho-mqtt
- psycopg2-binary
- Mosquitto MQTT broker
- PostgreSQL
- Grafana

## Screenshots

**Subscriber console:**
![Subscriber](screenshots/subscriber.png)

**PostgreSQL table:**
![PostgreSQL](screenshots/postgresql.png)

**Grafana Dashboard:**
![Grafana](screenshots/grafana_dashboard.png)

## Notes
- Make sure Mosquitto broker is running before starting subscriber and publisher.
- Ensure PostgreSQL database and table exist before running subscriber.
- Grafana panels are configured to refresh every 5 seconds for real-time visualization.







