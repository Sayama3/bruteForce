caractere = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j",
             "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
             "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X",
             "Y","Z","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<",
             "=",">","?","@","[","]","^","_","`","{","|","}","~","\\"," "]

def motAleatoire(caractere):
    import random
    motDePasse = str()
    nbrDeCaractere = random.randrange(5,20,1)
    for i in range(nbrDeCaractere):
        choix = random.randrange(0,94,1)
        motDePasse += caractere[choix]
    return motDePasse
