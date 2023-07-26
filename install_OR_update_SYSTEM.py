import ujson
from ds3231 import DS3231

rtc = DS3231(sdapin=21, sclpin=22) # инициализация аппаратных часов

# Пути к файлу файлу конфигурации
file_path = 'userSettings.json'

#### ----don't touch------- DEFAULT WiFi VARIABLES ----don't touch-------- ####
ap_ssid = "ESP32_HFF-AP"
ap_password = "1234567890"
client_ssid = "set_your_wifi_SSID"
client_password = "set_your_wifi_password"
gitflow_system = "main"
gitflow_updater= "main"
#### ----don't touch---- END OF DEFAULT WiFi VARIABLES ----don't touch---- ####


def save_default_settings(ap_ssid, ap_password, client_ssid, client_password):
    blank1 = {
        'ssid': ap_ssid,
        'password': ap_password
    }
    blank2 = {
        'ssid': client_ssid,
        'password': client_password
    }
    blank3 = {
        'gitflow': gitflow_system
    }
    blank4 = {
        'gitflow': gitflow_updater
    }
    data = {                                    # серилизация значений в строку для последующей записи
        'wifi_AP_settings': blank1,
        'wifi_Client_settings': blank2,
        'system_settings': blank3,
        'systemUpdater_settings': blank4
    }
    with open(file_path, 'w') as file:
        ujson.dump(data, file)

# чтение Config.json
def load_settings():
    try:
        with open(file_path, 'r') as file:
            return ujson.load(file)
    except OSError:
        print("Файл конфигурации модуля не найден")
        return None


def uptime():
    print('Система uptime: ', rtc.datetime())
    print('System boot: ', rtc.datetime())
    print('System current time: ', rtc.datetime())


# Если нет файла config.json или в нем нет нужных секций с переменными --> создаем необходимое c дефолтовыми значениями
def checkConfigFiles():
    try:
        with open(file_path, 'r') as file:
            pass  # Файл существует, ничего не делаем
    except OSError:
        print("Файл конфигурации модуля не найден.")
        print("Создание нового файла конфигурации со значениями по умолчанию: {}".format(file_path))
        with open(file_path, 'w') as file:
#            pass  # Создаем пустой файл
            str = print('#фаил конфигурации создан: ', rtc.datetime())
            file.write(str)
        save_default_settings(ap_ssid, ap_password, client_ssid, client_password)