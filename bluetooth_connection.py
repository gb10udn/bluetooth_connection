import subprocess
import configparser
import questionary

# subprocess.Popen("ping")

def connect(device_name: str):
    """
    A2DP で bluetooth 接続する関数。
    """
    cmd = f'btcom -n "{device_name}" -c -s110B'  # INFO: 240204 require https://bluetoothinstaller.com/bluetooth-command-line-tools
    subprocess.run(cmd)


def disconnect(device_name: str):
    """
    A2DP で bluetooth 切断する関数。
    """
    cmd = f'btcom -n "{device_name}" -r -s110B'
    subprocess.run(cmd)


def read_device_name_from_config(*, path='config.ini') -> str:
    """
    コンフィグファイルから
    """
    try:
        config_ini = configparser.ConfigParser()
        config_ini.read(path, encoding='utf-8')  # FIXME: 240129 コンフィグのパスがない場合のハンドリングを記述する。(他にも参照している箇所があった気がする。)
        return config_ini['GENERAL']['device_name']
    
    except:
        return None


if __name__ == '__main__':
    action = questionary.select(
        'Select bluetooth action',
        choices=['connect', 'disconnect'],  # TODO: 240204 現状のステータスを呼べるようにしてもいいかも？
    ).ask()