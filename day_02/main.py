import fileinput

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def getGamePower(input_file:str)->int:
    totalPower = 0
    with(fileinput.input(files=input_file, encoding="utf-8")) as f:
        for line in f:
            gameValid = True
            gameIdIndex = line.find(":")
            gameId = int(line[gameIdIndex-2] + line[gameIdIndex-1])
            gameData = line[gameIdIndex+2:].replace("\n", "").split("; ")
            power = 0

            redMax = 0;
            greenMax = 0;
            blueMax = 0

            for game in gameData:
                handFull = game.split(", ")
                for balls in handFull:
                    ball = balls.split(" ")
                    amount = int(ball[0])
                    match ball[1]:
                        case "red":
                            if (amount > redMax):
                                redMax = amount
                        case "blue":
                            if (amount > blueMax):
                                blueMax = amount
                        case "green":
                            if (amount > greenMax):
                                greenMax = amount
                
            power = redMax * greenMax * blueMax
            totalPower += power

    return totalPower;

def main():
    print(getGamePower("input.txt"))

if __name__ == "__main__":
    main()