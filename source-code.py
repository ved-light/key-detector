import msvcrt as ms
import time as t

def key_detector():
    
    print("\nPress keys to see their representation.\nPress 'q' to quit.\n")

    while True:
        if ms.kbhit():
        
            key=ms.getch()
        
            if key == b'\t': 
                key_value="TAB"
            elif key == b'\r': 
                key_value="ENTER"
            elif key == b' ': 
                key_value="SPACE"
            elif key==b'\x1b': 
                key_value="ESCAPE"
            elif key==b'\x08': 
                key_value="BACKSPACE"
            else:
                try: 
                    key_value=key.decode()
                except: 
                    key_value=str(key)
            
            msg = f"key pressed: {key_value}"
            
            for i in msg:
                t.sleep(0.02)
                print(i, end="", flush=True)
                
            print()

            if key==b'q':
                print("\nExiting...\n")
                break
            
if __name__ == "__main__":
    key_detector()
    