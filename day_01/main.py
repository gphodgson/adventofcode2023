import fileinput

numMap = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
        "zero" : "0"
    }

def getCalibration(input_file:str) -> int:
    runningTotal = 0
    with(fileinput.input(files=(input_file), encoding="utf-8")) as f:
        for line in f:
            firstNum = ""
            lastNum = ""
            print("-----------")
            print(line)
            line = replace_multiple(line, numMap)
            print(line)

            for char in line:
                if(char.isnumeric()):
                    firstNum = char
                    break
            for char in reversed(line):
                if(char.isnumeric()):
                    lastNum = char
                    break

            print(firstNum + lastNum)
            runningTotal+= int(firstNum + lastNum)

    return runningTotal


def replace_multiple(input_string:str, replacements:dict)->str:
    for old, new in replacements.items():
        input_string = input_string.replace(old, new)
    return input_string



def main():
    print(getCalibration("test.txt"))

if __name__ == "__main__":
    main()