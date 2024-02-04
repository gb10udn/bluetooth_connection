import subprocess
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


if __name__ == '__main__':
    command = questionary.select(
        'Select bluetooth action',
        choices=['connect', 'disconnect'],
    ).ask()