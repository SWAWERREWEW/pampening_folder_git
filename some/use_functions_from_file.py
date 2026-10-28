def print_nine(): print(9)
def print_one(): print(1)

def main():
    # sys.argv — это список всех слов, которые вы ввели в терминале после "python"
    # sys.argv[0] — это всегда имя самого файла ('main.py')
    # sys.argv[1] — это первое слово-команда после имени файла
    # sys.exit(1) - это выход

    import sys
    try: command = sys.argv[1]
    except IndexError: command = None
    
    if command == "print_nine":
        print_nine()
        exit()
    elif command == "print_one":
        print_one()
        exit()
    else:
        print_nine()
        print_one()

def short_sequence():
    num = 1
    while num < 5:
        yield num
        num += 1

for step in short_sequence():
    print(step)

if __name__ == "__main__":
    main()
