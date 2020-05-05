import pandas as pd
from random import randint
import datetime
import os


# Load both the sensors data in a zone and save them
def save_warehouse_zone_data(warehouse_name, warehouse_zone):
    # Reading data from top sensor in the zone
    top_sensor = os.path.join(".",warehouse_name,warehouse_zone,"top.csv")
    bottom_sensor = os.path.join(".",warehouse_name,warehouse_zone,"bottom.csv")
    zone_top = pd.read_csv(top_sensor)
    zone_top.rename({'Unnamed: 0':'date'}, axis=1, inplace=True)
    zone_top['date'] = pd.to_datetime(zone_top.date)
    # Reading data from the bottom sensor in the zone
    zone_bottom = pd.read_csv(bottom_sensor)
    zone_bottom.rename({'Unnamed: 0':'date'}, axis=1, inplace=True)
    zone_bottom['date'] = pd.to_datetime(zone_bottom.date)
    warehouse_zone_data = zone_top
    warehouse_zone_data['zone2_temparature'] = zone_bottom['temparature']
    warehouse_zone_data['average_temparature'] = warehouse_zone_data[['temparature', 'zone2_temparature']].mean(axis=1)
    warehouse_zone_data.to_csv(os.path.join(".",warehouse_name,warehouse_zone,"warehousedata.csv"), header=True, index=False)


def generate_censordata(sensor_location, sensor_id, high_temparature, low_temparature, warehouse_name, warehouse_zone):
    file_path = os.path.join('.', warehouse_name, warehouse_zone, sensor_location + ".csv")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after = today + datetime.timedelta(days=2)
    # start='1/10/2020', end='3/3/2020'
    date_rng = pd.date_range(start='1/10/2020', end=today, freq='30T')
    my_list = []
    for _ in range(len(date_rng)):
        my_list.append(randint(low_temparature - 3, high_temparature + 3))
    data = pd.DataFrame(index=date_rng)
    data['temparature'] = my_list
    data['ZID'] = warehouse_zone
    data['WID'] = warehouse_name
    data['sensorplace'] = sensor_location
    # data_final = data.iloc[:1]
    data.to_csv(file_path, index=True, header=True)


def generate_sensors_data():
    # Creating data for warehouse 1 zone 1 top sensor
    generate_censordata(sensor_id='s1', sensor_location='top', warehouse_zone='zone1', warehouse_name = 'wh1',
                      high_temparature=39, low_temparature=32)

    # Creating data for warehouse 1 zone 1 bottom sensor
    generate_censordata(sensor_id='s2', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh1',
                      high_temparature=39, low_temparature=32)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name = 'wh1')

    # Creating data for warehouse 1 zone 2 top sensor
    generate_censordata(sensor_id='s3', sensor_location='top', warehouse_zone='zone2', warehouse_name = 'wh1',
                      high_temparature=54, low_temparature=50)

    # Creating data for warehouse 1 zone 2 bottom sensor
    generate_censordata(sensor_id='s4', sensor_location='bottom', warehouse_zone='zone2', warehouse_name='wh1',
                      high_temparature=54, low_temparature=50)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh1')

    # Creating data for warehouse 2 zone 1 top sensor
    generate_censordata(sensor_id='s5', sensor_location='top', warehouse_zone='zone1', warehouse_name= 'wh2',
                      high_temparature=0, low_temparature=-20)

    # Creating data for warehouse 2 zone 1 bottom sensor
    generate_censordata(sensor_id='s6', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh2',
                      high_temparature=0, low_temparature=-20)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name='wh2')

    # Creating data for warehouse 2 zone 2 top sensor
    generate_censordata(sensor_id='s7', sensor_location='top', warehouse_zone='zone2', warehouse_name= 'wh2',
                      high_temparature=50, low_temparature=45)

    # Creating data for warehouse 2 zone 2 bottom sensor
    generate_censordata(sensor_id='s8', sensor_location='bottom', warehouse_zone='zone2', warehouse_name= 'wh2',
                      high_temparature=50, low_temparature=45)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh2')

    # Creating data for warehouse 3 zone 1 top sensor
    generate_censordata(sensor_id='s9', sensor_location='top', warehouse_zone='zone1', warehouse_name='wh3',
                      high_temparature=39, low_temparature=32)

    # Creating data for warehouse 3 zone 1 bottom sensor
    generate_censordata(sensor_id='s10', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh3',
                      high_temparature=39, low_temparature=32)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name='wh3')

    # Creating data for warehouse 3 zone 2 top sensor
    generate_censordata(sensor_id='s11', sensor_location='top', warehouse_zone='zone2', warehouse_name = 'wh3',
                      high_temparature=54, low_temparature=50)

    # Creating data for warehouse 3 zone 2 bottom sensor
    generate_censordata(sensor_id='s12', sensor_location='bottom', warehouse_zone='zone2', warehouse_name= 'wh3',
                      high_temparature=54, low_temparature=50)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh3')


    # Creating data for warehouse 4 zone 1 top sensor
    generate_censordata(sensor_id='s13', sensor_location='top', warehouse_zone='zone1', warehouse_name='wh4',
                      high_temparature=0, low_temparature=-20)

    # Creating data for warehouse 4 zone 1 bottom sensor
    generate_censordata(sensor_id='s14', sensor_location='bottom', warehouse_zone='zone1', warehouse_name = 'wh4',
                      high_temparature=0, low_temparature=-20)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name='wh4')

    # Creating data for warehouse 4 zone 2 top sensor
    generate_censordata(sensor_id='s15', sensor_location='top', warehouse_zone='zone2', warehouse_name='wh4',
                      high_temparature=50, low_temparature=44)

    # Creating data for warehouse 4 zone 2 bottom sensor
    generate_censordata(sensor_id='s16', sensor_location='bottom', warehouse_zone='zone2', warehouse_name = 'wh4',
                      high_temparature=50, low_temparature=44)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh4')

def generate_censordata_append(sensor_location, sensor_id, high_temparature, low_temparature, warehouse_name, warehouse_zone):
    file_path = os.path.join('.', warehouse_name, warehouse_zone, sensor_location + ".csv")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after = today + datetime.timedelta(days=2)
    # start='1/10/2020', end='3/3/2020'
    date_rng = pd.date_range(start=today, end=tomorrow, freq='30T')
    my_list = []
    for _ in range(len(date_rng)):
        my_list.append(randint(low_temparature - 3, high_temparature + 3))
    data = pd.DataFrame(index=date_rng)
    data['temparature'] = my_list
    data['ZID'] = warehouse_zone
    data['WID'] = warehouse_name
    data['sensorplace'] = sensor_location
    # data_final = data.iloc[:1]
    data.to_csv(file_path, mode='a', index=True, header=False)


def generate_sensors_data_append():
    # Creating data for warehouse 1 zone 1 top sensor
    generate_censordata_append(sensor_id='s1', sensor_location='top', warehouse_zone='zone1', warehouse_name = 'wh1',
                      high_temparature=39, low_temparature=32)

    # Creating data for warehouse 1 zone 1 bottom sensor
    generate_censordata_append(sensor_id='s2', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh1',
                      high_temparature=39, low_temparature=32)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name = 'wh1')

    # Creating data for warehouse 1 zone 2 top sensor
    generate_censordata_append(sensor_id='s3', sensor_location='top', warehouse_zone='zone2', warehouse_name = 'wh1',
                      high_temparature=54, low_temparature=50)

    # Creating data for warehouse 1 zone 2 bottom sensor
    generate_censordata_append(sensor_id='s4', sensor_location='bottom', warehouse_zone='zone2', warehouse_name='wh1',
                      high_temparature=54, low_temparature=50)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh1')

    # Creating data for warehouse 2 zone 1 top sensor
    generate_censordata_append(sensor_id='s5', sensor_location='top', warehouse_zone='zone1', warehouse_name= 'wh2',
                      high_temparature=0, low_temparature=-20)

    # Creating data for warehouse 2 zone 1 bottom sensor
    generate_censordata_append(sensor_id='s6', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh2',
                      high_temparature=0, low_temparature=-20)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name='wh2')

    # Creating data for warehouse 2 zone 2 top sensor
    generate_censordata_append(sensor_id='s7', sensor_location='top', warehouse_zone='zone2', warehouse_name= 'wh2',
                      high_temparature=50, low_temparature=45)

    # Creating data for warehouse 2 zone 2 bottom sensor
    generate_censordata_append(sensor_id='s8', sensor_location='bottom', warehouse_zone='zone2', warehouse_name= 'wh2',
                      high_temparature=50, low_temparature=45)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh2')

    # Creating data for warehouse 3 zone 1 top sensor
    generate_censordata_append(sensor_id='s9', sensor_location='top', warehouse_zone='zone1', warehouse_name='wh3',
                      high_temparature=39, low_temparature=32)

    # Creating data for warehouse 3 zone 1 bottom sensor
    generate_censordata_append(sensor_id='s10', sensor_location='bottom', warehouse_zone='zone1', warehouse_name='wh3',
                      high_temparature=39, low_temparature=32)

    save_warehouse_zone_data(warehouse_zone='zone1', warehouse_name='wh3')

    # Creating data for warehouse 3 zone 2 top sensor
    generate_censordata_append(sensor_id='s11', sensor_location='top', warehouse_zone='zone2', warehouse_name = 'wh3',
                      high_temparature=54, low_temparature=50)

    # Creating data for warehouse 3 zone 2 bottom sensor
    generate_censordata_append(sensor_id='s12', sensor_location='bottom', warehouse_zone='zone2', warehouse_name= 'wh3',
                      high_temparature=54, low_temparature=50)

    save_warehouse_zone_data(warehouse_zone='zone2', warehouse_name='wh3')
