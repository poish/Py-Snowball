from Window import Window
from Context import Context

class myContext(Context):
    def pressKeyB(self, mods):
        print("do something")

def main():

    okno = Window(640,480,"Moje okno")

    context = myContext("myContext")
    context.use()

    while not okno.shouldClose():

        okno.finalizeLoop()

    okno.terminate()

if __name__ == "__main__":
    main()