import spade
import cv2 as cv
import keyboard


def show(img):
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()



class MyAgent(spade.Agent.Agent):
    class CheckBehav(spade.Behaviour.Behaviour):
        def _process(self):

            print("aperte q para abrir")     
            try:
                if keyboard.is_pressed('q'):                
                    im = cv.imread("peppers_color.tif")
                    show(im)
            except Exception as E:
                print(E.message)

    def _setup(self):
        b = self.CheckBehav()
        self.addBehaviour(b, None)

if __name__ == "__main__":
	a = MyAgent("agent@127.0.0.1", "secret")
	a.start()
