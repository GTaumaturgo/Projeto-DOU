
import spade


class MyAgent(spade.Agent.Agent):
    class SimpleBehav(spade.Behaviour.OneShotBehaviour):
        def onStart(self):
            print("Hello")
        def _process(self):
            print("World!")
        def onEnd(self):
            print("Hehe!")

    def _setup(self):
        b = self.SimpleBehav()
        self.addBehaviour(b, None)


if __name__ == "__main__":
	a = MyAgent("agent@127.0.0.1", "secret")
	a.start()
