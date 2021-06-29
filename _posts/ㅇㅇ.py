
class HelloWorld :
    def __init__(self) :
        print("Helllo world! just one more time! ")
    def __del__(self) :
        print("Good bye!")
    def performAverage(self, val1, val2) :
        average = (val1 + val2) /2.0
        print("The average of the scores is : ", average)

def main() :
    world = HelloWorld()
    score1, score2 = map(int, input("Enter the scores : ").split())
    world.performAverage(score1, score2)

main()