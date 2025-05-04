import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    if os.getenv("FILENAME") is None or os.getenv("WORD") is None:
        print("Задайте переменные окружения FILENAME и WORD!")
        return 0

    filepath = os.getenv("FILENAME")
    word = os.getenv("WORD")

    f = open(filepath).readlines()

    for x in f:
        x = x.strip()
        if word in x:
            print(x)

main()