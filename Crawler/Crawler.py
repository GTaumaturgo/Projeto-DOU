import spade
import urllib2
import os
import datetime


def now_date_str(separator):
	now = datetime.datetime.now()
	day_str = ''
	month_str = ''
	if now.day >= 10:
		day_str = str(now.day)
	else:
		day_str = '0' + str(now.day)
	if now.month >= 10:
		month_str = str(now.month)
	else:
		month_str = '0' + str(now.month)
	return day_str + separator + month_str + separator + str(now.year)

class Crawler(spade.Agent.Agent):
	class CheckBehav(spade.Behaviour.OneShotBehaviour):
		def onStart(self):
			self.dirname = 'documents/' + now_date_str('-')
			if not os.path.exists(self.dirname):
				os.makedirs(self.dirname)
			self.url_prefix = 'http://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=515&pagina='
			self.url_suffix = '&data=' + now_date_str('/') + '&captchafield=firstAccess'

		def _process(self):
			for i in range(1,10000):
				url = self.url_prefix + str(i) + self.url_suffix
				print(url)
				response = urllib2.urlopen(url)
				conteudo = response.read()
				if 'DOCTYPE HTML' in conteudo:
					break
				try:
					file = open(self.dirname + '/' + 'document' + str(i) + '.pdf','wb')
					file.write(conteudo)
					file.close()
				except:
					print("sabia")
		def onEnd(self):
			print("Terminei")

	def _setup(self):
		
		b = self.CheckBehav()
		self.addBehaviour(b, None)

if __name__ == "__main__":
	a = Crawler('crawler@127.0.0.1', 'secret')
	a.start()
