import subprocess
import configparser
import questionary


def connect(device_name: str):    # TODO: 240204 HFP にも対応する。
    """
    A2DP で bluetooth 接続する関数。
    """
    cmd = f'btcom -n "{device_name}" -c -s110B'  # INFO: 240204 require https://bluetoothinstaller.com/bluetooth-command-line-tools
    subprocess.run(cmd)


def disconnect(device_name: str):  # TODO: 240204 HFP にも対応する。
    """
    A2DP で bluetooth 切断する関数。
    """
    cmd = f'btcom -n "{device_name}" -r -s110B'
    subprocess.run(cmd)


def read_device_name_from_config(*, path='config.ini') -> str | None:
    """
    コンフィグファイルから、対象のデバイス名を取得する関数。
    """
    try:
        config_ini = configparser.ConfigParser()
        config_ini.read(path, encoding='utf-8')
        return config_ini['GENERAL']['device_name']
    
    except:
        return None


if __name__ == '__main__':
    action = questionary.select(
        'Select bluetooth action',
        choices=['connect', 'disconnect'],  # TODO: 240204 現状のステータスを呼べるようにしてもいいかも？
    ).ask()

    device_name = read_device_name_from_config()
    if device_name is not None:
        if action == 'connect':
            connect(device_name)  # FIXME: 240204 失敗時の処理を書いてもいいかも？
        elif action == 'disconnect':
            disconnect(device_name)  # FIXME: 240204 失敗時の処理を書いてもいいかも？
        else:
            raise Exception('InternalError:')
    
    else:
        raise Exception('Failure: cannot obtain "device name" from "config.ini" ...')