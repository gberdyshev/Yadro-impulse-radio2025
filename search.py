from dotenv import dotenv

def main():
    if len(sys.argv) != 3:
        print("Введите аргументы в формате <имя_файла> <слово_для_поиска>")
        return 0

    filepath = sys.argv[1]
    word = sys.argv[2]

    f = open(filepath).readlines()

    for x in f:
        x = x.strip()
        if word in x:
            print(x)

main()