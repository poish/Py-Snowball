from Window import Window


def main():

    okno = Window(640,480,"Moje okno")

    while not okno.shouldClose():

        okno.finalizeLoop()

    okno.terminate()

if __name__ == "__main__":
    main()