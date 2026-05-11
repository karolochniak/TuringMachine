class Turing:
  
  def __init__(self, instrukcje):
    self.tasma = None 
    self.koniec = None 
    self.instrukcje = instrukcje 
    self.dict_instrukcje = None
    self.glowica = None 
    self.ruch_glowica = 0
    self.tasma_conv = []
    self.stan = None

  def odczyt_pliku(self):
    inst = {}
    zp = ""
    with open(self.instrukcje, 'r') as plik:
      for wiersz in plik:
        if wiersz[0] == '!':
          if wiersz.split()[1] == "input":
            self.tasma = wiersz.split()[2]
            continue
          if wiersz.split()[1] == "start_state":
            self.stan =  wiersz.split()[2]
            continue
          if wiersz.split()[1] == 'Koniec':
            self.koniec = wiersz.split()[1]
            continue
        if wiersz[0] == '%':
          zp = wiersz.split()[1]
          inst[zp] = {}
          tmp = inst[zp]
          continue
        try:
          ob_znak, zapis, kierunek, stan = wiersz.split()
        except:
          continue
        tmp[ob_znak] = (zapis, kierunek, stan)
    plik.close()
    self.dict_instrukcje = inst

  def modif_tasma(self, extend):
    self.tasma = ["$"] * extend + list(self.tasma) + ["$"] * extend
    self.ruch_glowica = extend  

  def ruch_tasma(self,ob_znak):
    zapis,kierunek,stan = self.dict_instrukcje[self.stan][ob_znak]
    if kierunek == "R":
      self.ruch_glowica +=1
    elif kierunek == "L":
      self.ruch_glowica -=1
    return self.ruch_glowica
      
  def konwersja_tasma_bis(self):
    self.tasma_conv = "".join([elem for elem in self.tasma if elem != "$"])
    self.tasma = self.tasma_conv
    
  def odczyt_tasma(self):
    self.odczyt_pliku()
    self.modif_tasma(15)
    while self.stan not in ["acc", "rej"]:
      self.glowica = self.tasma[self.ruch_glowica]
      zapis,kierunek,stan = self.dict_instrukcje[self.stan][self.glowica]
      self.tasma[self.ruch_glowica] = zapis
      self.ruch_glowica = self.ruch_tasma(self.glowica)
      self.stan = stan
    self.konwersja_tasma_bis()
    print("Wynik na taśmie:", self.tasma)
    if self.stan == "acc":
      print("Liczba jest podzielna przez 3")
    else:
      print("Liczba NIE jest podzielna przez 3.")
    return

t = Turing("podzielnosc3.txt")
t.odczyt_tasma()
