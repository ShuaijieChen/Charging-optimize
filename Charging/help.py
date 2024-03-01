import random
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

class Vehicle:
    # This class is used to represent vehicles
    """
        :param battery_capacity(KWh): double
            description: Maximum capacity of vehicle battery
        :param start_time: datetime
            description: The time the owner began using the vehicle
        :param end_time: datetime
            description: The time when the vehicle owner finishes using the vehicle
        :param parking_lot: object
            description: The parking lot where the vehicle is parked
        :param battery_level(KWh): double
            description: The current available electricity consumption of the vehicle
        :param charging_power(KW): int
            description: The charge and discharge power of the vehicle
    """
    def __init__(self, start_time, end_time, parking_lot=None, battery_capacity=77.0, battery_level=77.0, charging_power=20):
        self.start_time = start_time
        self.end_time = end_time
        self.battery_capacity = battery_capacity
        self.battery_level = battery_level
        self.charging_power = charging_power

    #充电一小时
    def charge(self, price):
        temp = self.battery_level
        if self.battery_level <= self.battery_capacity - 20:
            self.battery_level += 20
        else:
            self.battery_level = self.battery_capacity
        return 0 - (self.battery_level - temp) * price
    
    #放电一小时
    def discharge(self,price):
        temp = self.battery_level
        if self.battery_level >= 20:
            self.battery_level -= 20
        else:
            self.battery_level = 0
        return 0 - (self.battery_level - temp) * price
    
    def __str__(self):
        return f'Vehicle: {self.battery_capacity}, {self.start_time}, {self.end_time}'
    
    

def generate_random_time(start_hour, end_hour):
    hour = random.randint(start_hour, end_hour)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.now().replace(hour=hour, minute=minute, second=second)

def calculate_real_time(start_time, end_time):
    real_start_time = (start_time + timedelta(hours = 1))
    real_start_time = real_start_time.replace(minute=0, second=0)
    real_end_time = (end_time - timedelta(hours = 0))
    real_end_time = real_end_time.replace(minute=0, second=0)

    print ("next hour=",real_start_time.strftime('%H:%M:%S'))
    print ("prev hour=",real_end_time.strftime('%H:%M:%S'))
    return real_start_time, real_end_time

#读取一天（即24小时）的电价
def read_e_price(start, end):
    df_prices = pd.read_csv("GR-data-11-20.csv", header=None, names=["DateTime", "ElectricityPrice"])
    one_day_prices_list = df_prices["ElectricityPrice"][start:end].tolist()

    print(one_day_prices_list)
    print(len(one_day_prices_list))
    return one_day_prices_list