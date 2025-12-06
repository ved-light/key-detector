
def key_detector():
    
    import msvcrt as ms
    import time as t
    
    print("\nPress keys to see their representation.\nPress 'q' to quit.\n")

    while True:
        if ms.kbhit():
        
            key=ms.getch()
        
            if key == b'\t': b="TAB"
            elif key == b'\r': b="ENTER"
            elif key == b' ': b="SPACE"
            elif key==b'\x1b': b="ESCAPE"
            elif key==b'\x08': b="BACKSPACE"

            else:
                try: b=key.decode()
                except: b=str(key)
            
            msg="Key pressed: "+ b
            
            for i in msg:
                t.sleep(0.02)
                print(i, end="", flush=True)
                
            print()

            if key==b'q':
                print("Exiting...")
                break
            
if __name__ == "__main__":
    key_detector()
    