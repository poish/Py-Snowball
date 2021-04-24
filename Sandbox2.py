from Snowball import Snowball
from Context import Context

class cameraControl(Context):
    def pressKeyW(self, mods):
        print("up")

    def pressKeyA(self, mods):
        print("left")

    def pressKeyS(self, mods):
        print("down")

    def pressKeyD(self, mods):
        print("right")

class myApp(Snowball):
    def setup(self):

        vc = cameraControl("viewControl")
        vc.use()

    def loop(self):
        pass



m = myApp()
m.run()

