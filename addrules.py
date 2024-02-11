import sqlite3

def create_table():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Badminton(
        sport_name TEXT NOT NULL,                  
        sport_info TEXT NOT NULL,
        page2 TEXT NOT NULL,
        page3 TEXT,
        page4 TEXT,
        page5 TEXT,
        media1 BLOB,
        media2 BLOB,
        media3 BLOB,
        media4 BLOB,
        media5 BLOB
    )""")
    conn.commit()
    conn.close()
    print("Database created successfully!")
create_table()
def add_sport(sport_name):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Badminton
                    VALUES("Badminton", "Badminton is one of the most popular sports in the world, with a passionate fan following around the globe.\n\nIt is also one of the biggest draws at multi-sport spectacles like the Olympics.\n\nA regular fixture since the Barcelona 1992 Olympics, badminton now has five disciplines at the Games after mixed doubles was introduced at Atlanta 1996.\n\nChina has since emerged as the sport's dominant force with a total of 20 golds, 12 silvers and 15 bronze medals at the Olympics. Indonesia are second with eight golds, six silvers and seven bronze medals.\n\nWhile badminton is most popular in Asia, it also attracts great interest in Europe with players from Denmark among those regularly challenging for top honours.\n\nWant to learn more about badminton? Here’s a look at the rules and equipment you need to play.", "As outlined by the Badminton World Federation (BWF), here is a simplified rundown of the rules of badminton.

Badminton can be played either as singles or doubles. In singles, there are two players competing against each other. In doubles, two pairs of players form teams and compete against each other, resulting in a game of four players.Badminton scoring system
All singles and doubles matches are the best-of-three games. The first side to 21 points wins a game.\nA shuttlecock is hit over the net and into the opponent's court with a racquet.\n\nA point is scored on every serve and awarded to whichever side wins the rally. The winning side gets the next serve.\n\nIf the score is 20-20, a side must win by two clear points to win the game. If it reaches 29-29, the first to get their 30th point wins.", "Change of ends in badminton\n\n\nIn badminton, players are required to change ends under specific conditions. They should change ends at the conclusion of the first game. If a third game is required, they should also change ends at the end of the second game. In the third game, the change of ends occurs when one side reaches a score of 11 points.\n\n\n Winning a point in badminton\n\n\nA point is won if the birdie (shuttlecock) hits the ground in the opponent’s half of the court, including the lines. A point can therefore be conceded if a shot goes outside the court boundaries, if the birdie hits the net or passes through/under it, or if a player strikes the birdie twice with their racket.

Players must wait for the birdie to cross the net before playing a shot, and while you can follow through over it, touching the net with your body or racket results in a point being conceded.", "How to serve in badminton
The birdie must be hit below waist height, with players serving diagonally into their opponent’s service box. Both players must remain stationary until the serve is made.

As per badminton singles rules, the server starts from the right service court, and will serve from that side every time they have an even amount of points. A player serves from the left every time they have an odd amount of points.

Each player will retain serve for as long as they keep winning points.

In badminton doubles, the server will start on the right-hand side and keep serving, while alternating sides with their team-mate, so long as they keep winning points.

If the receiving side takes the point, they assume serve. Going forward, the player who did not initially serve for each team will only assume the service once their side has won a point as the receiving side.", "What is a badminton court’s dimensions?
In singles, a badminton court is 13.41m (44ft) long and 5.18m (17ft) wide. The width extends to 6.1m (20ft) in doubles.

The net is 1.55m (5ft 1in) high at the ends and 1.52m high (5ft) where it dips in the middle.

A serve must pass the short service line, which is 1.98m (6.5ft) from the net.

Beyond the short service line, there is a line which runs down the middle to split the left and right service courts. There is also a doubles service line 0.76m (2.5ft) in from the baseline.

That means each service court (four in total) is 3.96m (13ft) long and 2.59m (8.5ft) wide.", NULL , NULL, NULL, "assets\badminton-drive-serve-like-a-boss-badmintonserve.mp4", "assets\dimensions.png")""")

    conn.commit()   
    conn.close()
    print("Sport added successfully!")

add_sport('Badminton')


    