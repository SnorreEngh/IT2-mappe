class Bruker:
    """ Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn

    """
    def __init__(self, epost, fornavn, etternavn):
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker):
    """ Subklasse som henter fra Superklassen Brukere. Denne klassen brukes direkte
    
    Attributes:
        lønnskonto: Et heltal med brukerens lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto

class Faglærer(Lærer):
    """Subklasse til både Lærer og Bruker

    Attributes:
        kompetanse: En liste som inneholder hvilke fag læreren kan ha 
        klasser: En liste som inneholder hvilke klasser en lærer har ansvar for 
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

        def sett_karakter():
            pass

class Kontaktlærer(Lærer):
    """ subklasse til både Lærer og Bruker

    Attributes:
        klasse: En string med lærernes kontaktklasse
        trinn: Et heltall med hvilket trinn kontaktklassen til lærernen er
    """
    def __init__(self, klasse, trinn, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse = klasse
        self.trinn = trinn

        def fiks_fravær():
            pass

class Elev(Bruker):
    """ Subklasse til bruker

    Attributes:
        trinn: hvilket trinn eleven går på (str)
        klasse: hvilken klasse eleven går i (str)
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self.trinn = trinn
        self.klasse = klasse

    def lever_egenmelding(self):
        print(f"eleven med navn {self.fornavn} {self.epost} leverer egenmelding")



# Denne brukes for testing, betyr at koden inne i if-setningen 
# kun kjøres hvis vi "tykker" play på denne fila eller kjører denne fila i terminalen


if __name__ == "__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()
    ravi.logg_ut()
    
    snorre = Elev("snorreen@viken.no", "snorre", "engh", 3, "3STD")
    snorre.logg_inn()
    snorre.logg_ut