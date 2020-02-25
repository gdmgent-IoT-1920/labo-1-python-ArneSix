# Maak het programma LINGO met de gebruiker speelt. De game werkt als volgt:
# Genereer willekeurig een 4-cijferig nummer. Vraag de gebruiker om een ​​4-cijferig nummer te raden. 
# Voor elk cijfer dat de gebruiker correct op de juiste plaats heeft geraden , hebben ze een "kip". 
# Voor elk cijfer dat de correct geraden gebruiker op de verkeerde plaats is, is een 'ei'.
# Telkens wanneer de gebruiker een gok doet, vertel hem hoeveel "kip (of kippen)" en "ei (of eieren)" ze hebben.
# Als de gebruiker het juiste nummer heeft geraden, is het spel afgelopen. Houd het aantal beurten bij dat 
# de gebruiker maakt tijdens het spel en vertel de gebruiker aan het einde.
# Stel dat het door de computer gegenereerde nummer 1038 is. Een voorbeeld van een interactie kan er zo uitzien:

from Game import Game

chicken_game = Game()
chicken_game.startGame()
