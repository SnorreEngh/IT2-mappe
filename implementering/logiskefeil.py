# assert 10 > 5 # Siden 10 er større enn 5, derfor gjør denne ingenting 

# try:
#     assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmelding
# except:
#     print("dette er feil")


def areal(høyde, bredde):
    return høyde * bredde
def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

try:
    assert areal(3,2) == 6
    assert areal(3,3) == 9
    assert areal(3,4) == 12

    assert omkrets(3,2) == 10
    assert omkrets(3,3) == 12
    assert omkrets(3,4) == 14
except:
   print("her gikk noe galt, prøv med et positivt heltall")

print("koden er ferdig")