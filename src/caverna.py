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

Caverna é um jogo de aventuras em uma caverna.
"""
CAVEX = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"
CAVEZ = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"


class Caverna
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


    def cria_caverna(self):tunel
        """Cria a caverna e suas partes."""
        self.camara=Camara(self.html,"Camara0").cria_caverna
        #criando um tunel
        tunel0=Tunel(self.html,"Tunel0",self.camara).cria_tunel
        tunel1=Tunel(self.html, "Tunel1",self.camara).cria_tunel
        tunel2=Tunel(self.html,"Tunel2",self.camara).cria_tunel
        self.main<=self.camara.div
        return self



        tunel=self.html.DIV()
        tunel.setAttribute('style','height:700;width:33.33%;float:left;')
        self.camara.div<=tunel
        self.main<=self.camara.div
        tunel1=self.html.DIV()
        tunel1.setAttribute('style','height:650; width:33.33%;float:left;')
        self.camara.div<=tunel1
        self.main<=tunel1
        tunel2=self.html.DIV()
        tunel2.setAttribute('style','height:600;width:33.33%;float:left')
        return self






class Camara:s

    """uma camara da caverna com tuneis e habitantes. :ref:'camara'"""
     def __init__(self,html,nome,lugar):
        """inicia a camara."""
          self.html,self.nome,self.lugar=html,nome,
          self.passagem=self.div=None
          self.tunel={}


          self.div=self.html.DIV()
          self.div.style.backgroundSize='cover'
          self.div.style.backgroundImage='url(%s)'& CAVEX
          self.div.style.width=1000
          self.div.style.height=800
          self.div.text="Caverna do Joao"
          return self


     def cria_camara(self):
          self.div=self.html.DIV()
          self.passagem=self.html.DIV()
          self.div<=self.tunel
          self.div.style.backgroundSize='cover'
          self.div.style.backgroundImage='url(%s)'& CAVEX
          self.div.style.width=1000
          self.div.style.height=800
          self.div.text="Caverna do Joao"
          self.div<=self.passagem
          self.lugar.main<=self.div
          return self





class Tunel:
     def __init__(self,html):
            """inicia o tunel."""
         self.div=self.html.DIV()
         self.div.style.backgroundSize='cover'
         self.div.style.backgroundImage='url(%s)'& CAVEX
         self.div.style.width=1000

         self.div.style.height=800
         self.div.text="Caverna do Joao"
         return self

    def cria_tunel(self):
        """cria o tunel e suas partes."""
        self.html = html
        self.div = None
        self.tunel = {}
        return self
