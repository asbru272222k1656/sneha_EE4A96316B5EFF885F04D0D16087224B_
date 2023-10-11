class player:
  def play(self):
    print(" The Player is playing cricket.")
    class Batsman(player):
      def play(self):
        print(" The Batsman is batting.")
    class Bowler(player):
      def play(self):
        print(" The Bowler is bowling.")
    batsman=Batsman()
    bowler=Bowler()

    batsman.play()
    bowler.play()
              
             