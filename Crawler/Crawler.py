import spade
import urllib

class Crawler(spade.Agent.Agent):
	class CheckBehav(spade.Behaviour.OneShotBehaviour):
		def onStart(self):
			pass
        def _process(self):
            pass
        def onEnd(self):
            pass

	def _setup(self):
		b = self.CheckBehav()
		self.addBehaviour(b, None)

if __name__ == "__main__":
	a = Crawler("crawler@127.0.0.1", "secret")
	a.start()
