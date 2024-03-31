from engine.main import Game
import scriptblue
import scriptred
import scriptfinal

if __name__ == "__main__":
    G = Game((64, 64), scriptfinal, scriptred)
    G.run_game()