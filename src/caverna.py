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
        """Initializes builder and gui."""
        self.doc = gui.DOC
        self.html = gui.HTML
        self.camera = {}
        self.tunel = {}
        self.heroi = None
        self.main = self.doc['main']
        self.camara = None
        self.sala = None
        self.esconde = self.html.DIV()

    def movimenta(self, sala):
        self.esconde <= self.sala.div
        self.main <= sala.div
        self.sala = sala

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = Camara(self.html, "Camara0", self).cria_camara()
        #criando uma coleção de tuneis
        self.sala = self.camara

        self.tunel = {
            'tunel_%d' % a:
             Tunel(self.html, "tunel_%d" % a, self.camara, self.camara.passagem, self).cria_tunel()
             for a in range(0, 3)
        }
        return self

class Camara:

    """uma camara da caverna com tuneis e habitantes. :ref:'camara'
    """
    def __init__(self, html, nome, lugar):
        """inicia a camara."""
        self.html, self.nome, self.lugar = html, nome, lugar
        self.passagem = self.div = None
        self.tunel = {}

    def cria_camara(self):
        self.div = self.html.DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome)
        self.div.style.backgroundSize = 'cover'
        self.div.backgroundImage = 'url (%s)' % CAVEX
        self.div.style.width = 1000
        self.div.style.height = 800
        self.div.text = "Caverna do Joao"
        self.div <= self.passagem
        self.lugar.main <= self.div
        return self


class Tunel:
    """Um tunel da caverna que liga camaras. :ref:'tunel'
    """
    def __init__(self, html, nome, lugar, saida, caverna):
            """inicia o tunel."""
            self.html, self.nome, self.caverna = html, nome, caverna
            self.lugar, self.saida = lugar, saida
            self.entrada = self.passagem = self.div = None
            self.camara = {}

    def movimenta(self, ev):
        print(ev.target.Id)
        #self.caverna.movimenta(self)
        self.caverna.main <= self.div

    def sai_tunel(self):
        """cria uma saida deste tunel"""
        self.div = self.html.DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome)
        estilo = dict(
            width="33.33", heigth=300, float='left')
        self.entrada = self.html.DIV(
            Id='entra_'+self.nome, style=estilo
        )
        self.entrada.onclick = self.movimenta
        self.saida <= self.entrada
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEZ
        self.div.style.width=1000
        self.div.style.height=800
        self.div.text = "Caverna do João"
        return self

    def main(gui):
        print('Caverna 0.1.0')
        Caverna(gui).cria_caverna()

