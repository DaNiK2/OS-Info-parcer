#Импорт необходимых библиотек
import json
import platform
import os

os_name = platform.system() #Определяем в какой системе исполняется скрипт



def get_win_information(): #Получаем информацию о системе если скрипт исполняется на Win
    win_information = {
    'Platform': platform.platform(),
    'Version': platform.version(),
    'Processor': platform.processor(),
    'Cores': os.cpu_count(),
    'Architecture': platform.architecture()[0],
    }
    with open('win_information.json', 'w', encoding='utf-8') as f:
        json.dump(win_information, f, ensure_ascii=False, indent=4)
    for key, value in win_information.items():
        print(f'{key}: {value}')
    print('\nThe JSON file with system data has been saved!')

    return win_information




if os_name == "Windows":
    get_win_information()



# def get_win_information(): #Получаем информацию о системе если скрипт исполняется на Linux
#     lin_information = {
#     'Platform': platform.platform(),
#     'Version': platform.version(),
#     'Processor': platform.processor(),
#     'Cores': os.cpu_count(),
#     'Architecture': platform.architecture()[0],
#     }
#     print('Platform:', lin_information['Platform'])
#     print('Version:', lin_information['Version'])
#     print('Processor:', lin_information['Processor'])
#     print('Cores:', lin_information['Cores'])
#     print('Architecture:', lin_information['Architecture'])
#     return lin_information

# elif os_name == "Linux":
#     get_lin_information()
