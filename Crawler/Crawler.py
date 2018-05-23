import spade
import urllib2
url_prefix = "http://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=515&pagina="
url_suffix = "&data=23/05/2018&captchafield=firstAccess"

class Crawler(spade.Agent.Agent):
	class CheckBehav(spade.Behaviour.OneShotBehaviour):
		def onStart(self):
			pass
		def _process(self):
			for i in range(1,10000):
				url = url_prefix + str(i) + url_suffix
				response = urllib2.urlopen(url)
				if 'DOCTYPE HTML' in response.read():
					break
				file = open("documents/document" + str(i) + ".pdf",'wb')
				file.write(response.read())
				file.close()
		def onEnd(self):
			print("Hehe!")
			exit(0)

	def _setup(self):
		b = self.CheckBehav()
		self.addBehaviour(b, None)

if __name__ == "__main__":
	a = Crawler("crawler@127.0.0.1", "secret")
	a.start()
