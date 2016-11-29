
from bombstatus import BombSate


def main():

    bomb = BombSate()
    if bomb.cut_wires(['white', 'red', 'green', 'white']):
        print("Boom")
    else:
        print("Boom Defused")

    print()

main()
