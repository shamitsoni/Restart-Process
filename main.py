import os
import subprocess
import time
import keyboard


def is_process_running(process_name: str) -> bool:
    try:
        output = subprocess.check_output(f'tasklist | findstr {process_name}', shell=True).decode()
        return process_name in output
    except subprocess.CalledProcessError:
        return False


def restart_process(process_name: str, process_path: str) -> None:
    if is_process_running(process_name):
        # Terminate the process and delay 1s
        os.system(f'taskkill /f /im {process_name}')
        time.sleep(1)

    # Start the process
    subprocess.Popen(process_path)


def bind_key_to_restart(key: str, process_name: str, process_path: str) -> None:
    # Assigns the keybind to restarting the process
    keyboard.add_hotkey(key, lambda: restart_process(process_name, process_path))
    print(f'Press {key} to restart {process_name}')

    # Program won't call restart_process() until the keybind is pressed
    keyboard.wait()


def main() -> None:
    # Set up arguments
    name = 'explorer.exe'
    path = 'C:\\Windows\\explorer.exe'
    key = 'ctrl+alt+e'

    # Call
    bind_key_to_restart(key, name, path)


if __name__ == '__main__':
    main()
