import requests
# import folium
import random
import socket
import sys
import time

#Поиск IP
def Search_IP ():
    min1 = input ("Минимальное значение 1 (0 - 255): ")
    max1 = input (f"Максимальное значение 1 ({min1} - 255): ")

    min2 = input ("Минимальное значение 2 (0 - 255): ")
    max2 = input (f"Максимальное значение 2 ({min2} - 255): ")

    min3 = input ("Минимальное значение 3 (0 - 255): ")
    max3 = input (f"Максимальное значение 3 ({min3} - 255): ")

    min4 = input ("Минимальное значение 4 (0 - 255): ")
    max4 = input (f"Максимальное значение 4 ({min4} - 255): ")
    n = input ("Количество IP: ")
    n1 = 0

    while n1 < int(n):
        x1 = random.randint(int(min1),int(max1))
        x2 = random.randint(int(min2),int(max2))
        x3 = random.randint(int(min3),int(max3))
        x4 = random.randint(int(min4),int(max4))

        Pre_IP = (str(x1)+"."+str(x2)+"."+str(x3)+"."+str(x4))
        print (str(Pre_IP))
        n1 = int(n1) + 1

#Модифицированный поиск IP
def Search_IP_Moded ():
    min1 = input ("Минимальное значение 1 (0 - 255): ")
    max1 = input (f"Максимальное значение 1 ({min1} - 255): ")

    min2 = input ("Минимальное значение 2 (0 - 255): ")
    max2 = input (f"Максимальное значение 2 ({min2} - 255): ")

    min3 = input ("Минимальное значение 3 (0 - 255): ")
    max3 = input (f"Максимальное значение 3 ({min3} - 255): ")

    min4 = input ("Минимальное значение 4 (0 - 255): ")
    max4 = input (f"Максимальное значение 4 ({min4} - 255): ")
    
    n = input ("Количество IP: ")
    n1 = 0

    while n1 < int(n):
        x1 = random.randint(int(min1),int(max1))
        x2 = random.randint(int(min2),int(max2))
        x3 = random.randint(int(min3),int(max3))
        x4 = random.randint(int(min4),int(max4))

        Pre_IP = (str(x1)+"."+str(x2)+"."+str(x3)+"."+str(x4))
        n1 = int(n1) + 1

        Info_IP (Pre_IP)
        print ("")
        
#Информация об IP (Внктренняя)
def Info_IP_Log (ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
        '[IP]': response.get('query'),
        '[Int prov]': response.get('isp'),
        '[Org]': response.get('org'),
        '[Country]': response.get('country'),
        '[Region Name]': response.get('regionName'),
        '[City]': response.get('city'),
        '[ZIP]': response.get('zip'),
        '[Lat]': response.get('lat'),
        '[Lon]': response.get('lon')
        }
        return data
    except requests.exceptions.ConnectionError:
        return "Ошибка подключения"

#Сохранение IP
def Save_IP (ip):
    print ("Получение информации об IP...")
    f = open (f'{ip}_Save.txt','w')

    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
        '[IP]': response.get('query'),
        '[Int prov]': response.get('isp'),
        '[Org]': response.get('org'),
        '[Country]': response.get('country'),
        '[Region Name]': response.get('regionName'),
        '[City]': response.get('city'),
        '[ZIP]': response.get('zip'),
        '[Lat]': response.get('lat'),
        '[Lon]': response.get('lon')
        }
        for k, v in data.items():
            f.write (f'{k} : {v}' + '\n')

    except requests.exceptions.ConnectionError:
        print ("Ошибка подключения")
    print ("Файл создан!")
    f.close()

#Информация об IP (Внешняя)
def Info_IP (ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
        '[IP]': response.get('query'),
        '[Int prov]': response.get('isp'),
        '[Org]': response.get('org'),
        '[Country]': response.get('country'),
        '[Region Name]': response.get('regionName'),
        '[City]': response.get('city'),
        '[ZIP]': response.get('zip'),
        '[Lat]': response.get('lat'),
        '[Lon]': response.get('lon')
        }

        for k, v in data.items():
            print (f'{k} : {v}')
        
        #area = folium.map([response.get("lat"), response.get("lon")])
        #area.save(f'{response.get("country")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print ("Ошибка подключения")

#Подключение к IP
def Connect_IP(ip, otp, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (ip, int(port))
    print('Подключение к {} порт {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Set a timeout for the socket connection
        sock.settimeout(10)  # Set the timeout to 10 seconds

        # Отправка данных
        mess = otp
        print()
        print('Подключено к {} порт {}'.format(*server_address))
        print(f'Отправка: {mess}')
        message = mess.encode()
        sock.sendall(message)

        # Смотрим ответ
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            mess = data.decode()
            print(f'Получено: {data.decode()}')

    except socket.timeout:
        print('Превышено время ожидания')
    finally:
        print('Закрываем сокет')
        sock.close()

#Мониторинг IP
def Monitoring_IP (ip):
    Time = input ("Время мониторинга в секундах: ")
    while Time > "0":
        Info_IP (ip)
        print ("")
        time.sleep (1)
    print ("Мониторинг завершён!")

#Поиск IP с фильтрами
def Analitic_IP_Filter ():
    Filters = {}

    #Получение фильтров
    while 1 > 0:
        print()
        print ("--------------------------")
        print ("Фильтры")
        print ("1 - По номеру IP")
        print ("2 - По провайдеру IP")
        print ("3 - По организации IP")
        print ("4 - По стране IP")
        print ("5 - По региону IP")
        print ("6 - По городу IP")
        print ("7 - По почтовому номеру IP")
        print ("8 - По широте IP")
        print ("9 - По долготе IP")
        print ("S - Запуск поиска")
        print ("--------------------------")
        print()
        com = input("> ")

        if com == "1":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('fmin1', 'fmax1', 'fmin2', 'fmax2', 'fmin3', 'fmax3', 'fmin4', 'fmax4')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")

                else:
                    fmin1 = int(input("Минимальное значение 1 (0 - 255): "))
                    fmax1 = int(input(f"Максимальное значение 1 ({fmin1} - 255): "))

                    fmin2 = int(input("Минимальное значение 2 (0 - 255): "))
                    fmax2 = int(input(f"Максимальное значение 2 ({fmin2} - 255): "))

                    fmin3 = int(input("Минимальное значение 3 (0 - 255): "))
                    fmax3 = int(input(f"Максимальное значение 3 ({fmin3} - 255): "))

                    fmin4 = int(input("Минимальное значение 4 (0 - 255): "))
                    fmax4 = int(input(f"Максимальное значение 4 ({fmin4} - 255): "))

                    Filters['fmin1'] = int(fmin1)
                    Filters['fmax1'] = int(fmax1)
                    Filters['fmin2'] = int(fmin2)
                    Filters['fmax2'] = int(fmax2)
                    Filters['fmin3'] = int(fmin3)
                    Filters['fmax3'] = int(fmax3)
                    Filters['fmin4'] = int(fmin4)
                    Filters['fmax4'] = int(fmax4)
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['fmin1']
                    del Filters['fmax1']
                    del Filters['fmin2']
                    del Filters['fmax2']
                    del Filters['fmin3']
                    del Filters['fmax3']
                    del Filters['fmin4']
                    del Filters['fmax4']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")

        elif com == "2":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('fprov')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    fprov = input("Имя провайдера: ")

                    Filters['fprov'] = fprov
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['fprov']
                    print()
                    print("Фильтр отключён")
                else:
                     print()
                     print("Данный фильтр неактивен")
            
        elif com == "3":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('forg')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активирован")
                else:
                    forg = input("Имя организации: ")

                    Filters['forg'] = forg
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['forg']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "4":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('fcount')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    fcount = input("Название страны: ")

                    Filters['fcount'] = fcount
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['fcount']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "5":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('freg')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    freg = input("Название региона: ")

                    Filters['freg'] = freg
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['freg']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "6":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('fsity')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    fsity = input("Название города: ")

                    Filters['fsity'] = fsity
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['fsity']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "7":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('fzip')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    fzip = input("Почтовый номер: ")

                    Filters['fzip'] = fzip
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['fzip']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "8":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('flat1', 'flat2')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    flat1 = int(input("Минимальная широта (-90 - 90): "))
                    flat2 = int(input(f"Максимальная широта ({flat1} - 90): "))

                    Filters['flat1'] = flat1
                    Filters['flat2'] = flat2
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['flat1']
                    del Filters['flat2']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")
            
        elif com == "9":
            print ("")
            print ("1 - Добавить фильтр")
            print ("2 - Удалить фильтр")
            print ("")
            com = input("> ")
            key = ('flon1', 'flon2')

            if com == "1":
                keys = Filters.keys()

                if key in keys:
                    print()
                    print("Фильтр уже активен")
                else:
                    flon1 = int(input("Минимальная долгота (-180 - 180): "))
                    flon2 = int(input(f"Максимальная долгота ({flon1} - 180): "))

                    Filters['flon1'] = flon1
                    Filters['flon2'] = flon2
                    print()
                    print("Фильтр активирован")

            elif com == "2":
                keys = Filters.keys()

                if key in keys:
                    del Filters['flon1']
                    del Filters['flon2']
                    print()
                    print("Фильтр отключён")
                else:
                    print()
                    print("Данный фильтр неактивен")

        elif com == "S":
            break
            
        else:
            print ("Неизвестная команда!")

    #Проверка фильтров
    keys = Filters.keys()

    #Фильтр диапазона
    if all(key in keys for key in ('fmin1', 'fmax1', 'fmin2', 'fmax2', 'fmin3', 'fmax3', 'fmin4', 'fmax4')):
        fmin1 = Filters.get('fmin1')
        fmax1 = Filters.get('fmax1')
        fmin2 = Filters.get('fmin2')
        fmax2 = Filters.get('fmax2')
        fmin3 = Filters.get('fmin3')
        fmax3 = Filters.get('fmax3')
        fmin4 = Filters.get('fmin4')
        fmax4 = Filters.get('fmax4')
        print("Применён фильтр диапазона!")
    else:
        fmin1 = 0
        fmax1 = 255
        fmin2 = 0
        fmax2 = 255
        fmin3 = 0
        fmax3 = 255
        fmin4 = 0
        fmax4 = 255

    #Фильтр провайдера
    if all(key in keys for key in ('fprov')):
        fprov = Filters.get('fprov')
        print("Применён фильтр провайдера!")
    else:
        fprov = 'null'

    #Фильтр организации
    if all(key in keys for key in ('forg')):
        forg = Filters.get('forg')
        print("Применён фильтр организации!")
    else:
        forg = 'null'

    #Фильтр страны
    if all(key in keys for key in ('fcount')):
        fcount = Filters.get('fcount')
        print("Применён фильтр страны!")
    else:
        fcount = 'null'

    #Фильтр региона
    if all(key in keys for key in ('freg')):
        freg = Filters.get('freg')
        print("Применён фильтр региона!")
    else:
        freg = 'null'

    #Фильтр города
    if all(key in keys for key in ('fsity')):
        fsity = Filters.get('fsity')
        print("Применён фильтр города!")
    else:
        fsity = 'null'

    #Фильтр почтового индекса
    if all(key in keys for key in ('fzip')):
        fzip = Filters.get('fzip')
        print("Применён фильтр почтового индекса!")
    else:
        fzip = 'null'

    #Фильтр широты
    if all(key in keys for key in ('flat1','flat2')):
        flat1 = int(Filters.get('flat1'))
        flat2 = int(Filters.get('flat2'))
        print("Применён фильтр широты!")
    else:
        flat1 = -90
        flat2 = 90

    #Фильтр долготы
    if all(key in keys for key in ('flon1','flon2')):
        flon1 = int(Filters.get('flon1'))
        flon2 = int(Filters.get('flon2'))
        print("Применён фильтр долготы!")
    else:
        flon1 = -180
        flon2 = 180

    #Анализ
    ip1 = fmin1
    ip2 = fmin2
    ip3 = fmin3
    ip4 = fmin4
    
    summ = (fmax1 - fmin1 + 1) * (fmax2 - fmin2 + 1) * (fmax3 - fmin3 + 1) * (fmax4 - fmin4 + 1)
    print(f'Результатов после фильтра по номеру IP: {summ}')
    print("Поиск запущен...")

    Qwery = 0
    Limit = 4
    Sleep_Time = 2

    for i in range(summ - 1):
        if Qwery == Limit:
            time.sleep(Sleep_Time)
            Qwery = 0
        else:
            Qwery += 1

        score = 0
        ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
        Info = Info_IP_Log(ip)

        #Проверка
        if Info == 'Ошибка подключения':
            print()
            print(f"Не удалось получить информацию об {ip}!")

            ip4 += 1
            if ip4 == fmax4:
                ip4 = fmin4
                ip3 += 1
                if ip3 == fmax3:
                    ip3 = fmin3
                    ip2 += 1
                    if ip2 == fmax2:
                        ip2 = fmin2
                        ip1 += 1
                        if ip1 == fmax1:
                            print()
                            print("Поиск завершён!")
                            break
            continue

        elif ((Info["[City]"] == None) and (Info["[Country]"] == None) and (Info["[Int prov]"] == None) and (Info["[Lat]"] == None) and (Info["[Lon]"] == None) and (Info["[Org]"] == None) and (Info["[Region Name]"] == None) and (Info["[ZIP]"] == None)):
            print()
            print(f"{ip} пуст!")

            ip4 += 1
            if ip4 == fmax4:
                ip4 = fmin4
                ip3 += 1
                if ip3 == fmax3:
                    ip3 = fmin3
                    ip2 += 1
                    if ip2 == fmax2:
                        ip2 = fmin2
                        ip1 += 1
                        if ip1 == fmax1:
                            print()
                            print("Поиск завершён!")
                            break
            continue

        #Обработка фильтров
        if fprov != 'null':
            if Info['[Int prov]'] == fprov:
                score += 1

        if forg != 'null':
            if Info['[Org]'] == forg:
                score += 1

        if fcount != 'null':
            if Info['[Country]'] == fcount:
                score += 1

        if freg != 'null':
            if Info['[Region Name]'] == freg:
                score += 1

        if fsity != 'null':
            if Info['[City]'] == fsity:
                score += 1

        if fzip != 'null':
            if Info['[ZIP]'] == fzip:
                score += 1

        if Info['[Lat]'] != None:
            if flat1 <= int(Info['[Lat]']) <= flat2:
                score += 1

        if Info['[Lon]'] != None:
            if flon1 <= int(Info['[Lon]']) <= flon2:
                score += 1

        if score >= 1:
            for k, v in Info.items():
                print(f'{k} : {v}')


        ip4 += 1
        if ip4 == fmax4:
            ip4 = fmin4
            ip3 += 1
            if ip3 == fmax3:
                ip3 = fmin3
                ip2 += 1
                if ip2 == fmax2:
                    ip2 = fmin2
                    ip1 += 1
                    if ip1 == fmax1:
                        print()
                        print("Поиск завершён!")
                        break

#Меню
def Menu ():
    print ("")
    print ("Выбор функции")
    print ("1: Поиск IP")
    print ("2: Сохранение IP")
    print ("3: Информация об IP")
    print ("4: Подключение к IP")
    print ("5: Мониторинг IP")
    print ("6: Анализ IP")
    print ("1_Moded: Модифицированный поиск IP")
    print ("")
    com = input ("")
    if com == "1":
        Search_IP ()
    elif com == "1_Moded":
        Search_IP_Moded ()
    elif com == "2":
        ip1 = input ("Введите IP: ")
        Save_IP (ip1)
    elif com == "3":
        ip1 = input ("Введите IP: ")
        Info_IP (ip1)
    elif com == "4":
        ip1 = input ("Введите IP: ")
        otp1 = input ("Введите текст данных: ")
        port1 = input ("Введите номер порта: ")
        Connect_IP (ip1, otp1, port1)
    elif com == "5":
        ip1 = input ("Введите IP: ")
        Monitoring_IP (ip1)
    elif com == "6":
        Analitic_IP_Filter ()
    else:
        print ("Неизвестная команда!")

while 1 > 0:
    Menu()
