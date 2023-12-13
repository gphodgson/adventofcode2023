import fileinput

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def getIdSummation(input_file:str)->int:
    idSummation = 0
    with(fileinput.input(files=input_file, encoding="utf-8")) as f:
        for line in f:
            print("------")
            gameValid = True
            gameIdIndex = line.find(":")
            gameId = int(line[gameIdIndex-2] + line[gameIdIndex-1])
            gameData = line[gameIdIndex+2:].replace("\n", "").split("; ")
            for game in gameData:
                print(game)
                handFull = game.split(", ")
                for balls in handFull:
                    ball = balls.split(" ")
                    amount = int(ball[0])
                    match ball[1]:
                        case "red":
                            if (amount > RED_MAX):
                                gameValid = False
                                break
                        case "blue":
                            if (amount > BLUE_MAX):
                                gameValid = False
                                break
                        case "green":
                            if (amount > GREEN_MAX):
                                gameValid = False
                                break
                if(not gameValid):
                   print("bad game")
                   break

            if(gameValid):
                idSummation += gameId
                

    return idSummation;

def main():
    print(getIdSummation("input.txt"))

if __name__ == "__main__":
    main()