"""
############################################################
Caverna - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/11/04
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

Caverna eh um jogo de aventuras em uma caverna.
"""
CAVEX = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"
CAVEZ = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernaz.jpg"


class Caverna:
    """Uma caverna com cameras tuneis e habitantes. :ref:`caverna`
    """
    def __init__(self, gui):
        """Inicia a camara. """
        self.doc = gui.DOC
        self.html = gui.HTML
        self.camera = {}
        self.tunel = {}
        self.heroi = None
        self.main = self.doc['main']
        self.camara = None


    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = Camara(self.html, "Camara0").cria_caverna()
        #criando uma coleção de tunel

        self.tunel = {
            'tunel_%d' % a:
             Tunel(self.html, "tunel_%d" %a, self.camara).cria_tunel()
             for a in range(0, 3)
        }

        return self

class Camara:

    """uma camara da caverna com tuneis e habitantes. :ref:'camara'"""
     def __init__(self, html, nome, lugar):
        """inicia a camara."""
          self.html, self.nome, self.lugar = html, nome, lugar
          self.passagem = self.div = None
          self.tunel = {}

     def cria_camara(self):
          self.div = self.html.DIV(Id=self.nome)
          self.passagem = self.html.DIV(Id='passa_'+self.nome)
          self.div <= self.passagem
          self.div.style.backgroundSize = 'cover'
          self.div.backgroundImage = 'url &s)' %CAVEX
          self.div.style.width = 1000
          self.div.style.height = 800
          self.div.text = "Caverna do Joao"
          self.div <= self.passagem
          self.lugar.main <= self.div
          return self





class Tunel:
    def __init__(self, html, nome, lugar, saida):
            """inicia o tunel."""
        self.html, self.nome, self.lugar, self.saida = html, nome, lugar, saida
        self.passagem = self.div = None
        self.tunel = {}



    def cria_tunel(self):
        """cria o tunel e suas partes."""
        self.div = self.html.DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome
        self.entrada = self.html.DIV(Id='entra_'+self.nome, width='33.33%')
        self.saida <= self.entrada
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' %CAVEZ
        self.div.style.width=1000
        self.div.style.height=800
        self.div.text = "Caverna do João"
        return self


    def main(gui):
        print('Caverna 0.1.0')
        caverna=Caverna(gui).cria_caverna()

