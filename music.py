import time 
import sys 

def print_lyrics():
    lyrics = [
        "Arz kiya hai", 
        "Humne bhi likha kuch tere baare mein..",
        "Aise tu lage ki gulaab hai..",
        "Aur aise tu lage ki gulaab hai..",
    ]

    delays = [1.0, 0.1, 1.12, 0.9, 0.8]
    print("Arz Kiya Hai....:\n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i])

print_lyrics()

