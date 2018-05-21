import cv2 as cv
import spade


def show(img):
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


class Opener(spade.Agent.Agent):
	class ReceiveBehav(spade.Behaviour.Behaviour):
		"""This behaviour will receive all kind of messages"""

		def _process(self):
			self.msg = None

			# Blocking receive for 10 seconds
			self.msg = self._receive(True)


			# Check wether the message arrived
			if self.msg:
				print "I got a message!"
                im = cv.imread('peppers_color.tif')
                show(im)

	# class AnotherBehav(spade.Behaviour.Behaviour):
	# 	"""This behaviour will receive only messages of the 'cooking' ontology"""

	# 	def _process(self):
	# 		self.msg = None

	# 		# Blocking receive indefinitely
	# 		self.msg = self._receive(True)

	# 		# Check wether the message arrived
	# 		if self.msg:
	# 			print "I got a cooking message!"
	# 		else:
	# 			print "I waited but got no cooking message"

	def _setup(self):
		# Add the "ReceiveBehav" as the default behaviour
		rb = self.ReceiveBehav()
		# ab = self.AnotherBehav()
		self.setDefaultBehaviour(rb)

		# Prepare template for "AnotherBehav"
		# cooking_template = spade.Behaviour.ACLTemplate()
		# cooking_template.setOntology("cooking")
		# mt = spade.Behaviour.MessageTemplate(cooking_template)

		# # Add the behaviour WITH the template
		# self.addBehaviour(ab, mt)


if __name__ == "__main__":
	a = Opener("agent2@127.0.0.1", "secret")
	a.start()
