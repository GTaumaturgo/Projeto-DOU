import spade
import cv2 as cv
import keyboard


class Checker(spade.Agent.Agent):
	class CheckBehav(spade.Behaviour.Behaviour):
		def _process(self):
			print("voce quer abrir a imagem?")
			try:
				s = raw_input("")
				print(s)
				if s == "sim":
					print("mandei")
					# First, form the receiver AID
					receiver = spade.AID.aid(name="agent2@127.0.0.1", 
						addresses=["xmpp://agent2@127.0.0.1"])

					# Second, build the message
					self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
					# Set the "inform" FIPA performative
					self.msg.setPerformative("inform")
					# Set the ontology of the message content
					# self.msg.setOntology("myOntology")
					# Set the language of the message content
					self.msg.setLanguage("OWL-S")
					self.msg.addReceiver(receiver)            # Add the message receiver
					self.msg.setContent("abre a imagem ai")        # Set the message content
					self.myAgent.send(self.msg)

				
			except Exception as E:
				print(E.message)
	def _setup(self):
		b = self.CheckBehav()
		self.addBehaviour(b, None)


if __name__ == "__main__":
	a = Checker("agent1@127.0.0.1", "secret")
	a.start()
	
