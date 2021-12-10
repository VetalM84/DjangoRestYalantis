# Тестовое задание для Yalantis на Django Rest Framework

Створіть перелік відкритих (без аутентифікацій) endpoint'ів для наступних операцій:
Driver:
+ GET /drivers/driver/ - вивід списку водіїв
+ GET /drivers/driver/?created_at__gte=10-11-2021 - вивід списку водіїв, які створені після 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - вивід списку водіїв, котрі створені до 16-11-2021

+ GET /drivers/driver/<driver_id>/ - отримання інформації по певному водію
+ POST /drivers/driver/ - створення нового водія
+ UPDATE /drivers/driver/<driver_id>/ - редагування водія
+ DELETE /drivers/driver/<driver_id>/ - видалення водія

Vehicle:
+ GET /vehicles/vehicle/ - вивід списку машин
+ GET /vehicles/vehicle/?with_drivers=yes - вивід списку машин з водіями
+ GET /vehicles/vehicle/?with_drivers=no - вивід списку машин без водіїв

+ GET /vehicles/vehicle/<vehicle_id> - отримання інформації по певній машині
+ POST /vehicles/vehicle/ - створення нової машини
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - редагування машини
+ POST /vehicles/set_driver/<vehicle_id>/ - садимо водія в машину / висаджуємо водія з машини  
+ DELETE /vehicles/vehicle/<vehicle_id>/ - видалення машини
