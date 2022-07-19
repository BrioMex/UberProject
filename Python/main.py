from account import Account
from car import Car

if __name__ == "__main__":
    print('Hola mundo')
    
    car = Car('AMS234',Account('Manuel Briones','BIRM131285'))
    print(vars(car))
    print(vars(car.driver))