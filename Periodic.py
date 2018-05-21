
import spade


class MyAgent(spade.Agent.Agent):
	class SimpleBehav(spade.Behaviour.PeriodicBehaviour):
		
		def _onTick(self):
			print(self.myAgent.count)
			self.myAgent.count += 1
	def _setup(self):
		self.count = 0
		b = self.SimpleBehav(1)
		self.addBehaviour(b,None)



if __name__ == "__main__":
	a = MyAgent("agent@127.0.0.1", "secret")
	a.start()
