# iot-sensor-dashboard
IoT Sensor Data Collection and Visualization using MQTT, PostgreSQL, and Grafana. Simulated temperature and humidity sensor data is stored and visualized in real time.
---

## Description
The system includes:

- **Publisher**: Python script simulating sensor data (temperature & humidity) and sending it to an MQTT broker every 5 seconds.
- **Subscriber**: Python script subscribing to the MQTT topic and storing messages in PostgreSQL.
- **Visualization**: Grafana dashboard connected to PostgreSQL displaying live temperature and humidity graphs.

---

## Setup / Installation

1. **Install Python 3.13**  
   Download from [https://www.python.org](https://www.python.org) if not already installed.

2. **Install dependencies**  
   Open terminal or cmd in the project folder and run:

   ```bash
   pip install -r requirements.txt
   pip install paho-mqtt psycopg2-binary
3. **Start Mosquitto MQTT broker**
   ```bash
    C:\Program Files\mosquitto\mosquitto.exe"
4. **Prepare PostgreSQL database**
   Create database:

    ```sql
    CREATE DATABASE iot_data;
    
   Create table:
     ```sql
    CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature REAL,
    humidity REAL
);
6. **Run subscriber**
   In a new terminal:
   
   ```bash
   python mqtt_subscriber_pg.py
7. **Run publisher**
   In another terminal:
   ```sql
   python sensor_publisher.py
8. **Open Grafana**
Go to http://localhost:3000
Login: admin / sbaukajan2006
Add PostgreSQL as Data Source (Host: localhost:5432, Database: iot_data)
Create dashboard with two panels (temperature & humidity). Set refresh to 5s.
**Project Structure**
iot-sensor-dashboard/
├─ mqtt_subscriber_pg.py       # Subscriber script writing MQTT data to PostgreSQL
├─ sensor_publisher.py         # Publisher script simulating sensor data
├─ README.md                   # Project explanation and instructions
├─ requirements.txt            # Python dependencies
├─ screenshots/
│   ├─ subscriber.png          # Output from subscriber console
│   ├─ postgresql.png          # Example of PostgreSQL table
│   └─ grafana_dashboard.png   # Screenshot of Grafana dashboard
**Dependencies**
1)Python 3.13
2)paho-mqtt
3)psycopg2-binary
4)Mosquitto MQTT broker
5)PostgreSQL
6)Grafana
**Screenshots**
Subscriber console output:<img width="847" height="184" alt="subscriber" src="https://github.com/user-attachments/assets/40ffee96-7782-4c59-8226-88f110782319" />
PostgreSQL table content:<img width="553" height="196" alt="postgresql" src="https://github.com/user-attachments/assets/a954dae9-a7a9-40ee-a0ff-96977cf24f38" />
Grafana dashboard:<img width="1437" height="385" alt="grafana_dashboard" src="https://github.com/user-attachments/assets/96caaa16-81a8-4083-926f-3d1d88789789" />
**Notes**
1)Make sure Mosquitto broker is running before starting subscriber and publisher.
2)Ensure PostgreSQL database and table exist before running subscriber.
3)Grafana panels are configured to refresh every 5 seconds for real-time visualization.
4)This setup can be easily extended to real sensors or additional metrics.

