from cs50 import get_string
import random
#https://www.basketball-reference.com/leagues/NBA_2024_per_game.html
#https://www.espn.com/nba/stats/player
# I got the Random Library from https://docs.python.org/3/library/random.html
# CS50 library - https://manual.cs50.io/
print("NBA guessing game. You get four hints")
x = 4


def hint(x):
   if x == 4:
      print("This player's career high is " +player_high+ '.')
   elif x == 3:
      print("This player is a "+random_position+'.')


   elif x == 2:
       print("This player played at " + random_college + " before the NBA")










def check(random_college,random_position,teamate,random_player,x):


   while x > 0:
       response = get_string("Enter a guess: ")
       if response == random_player:
           print("You win!")
           break
       else:
           print("Incorrect")
           hint(x)
       x -= 1
       if x == 0:
           print("You lose! The player was " +random_player+ ".")


player_teamate = { 'Joel Embiid':'James Harden', 'Luka Doncic':'Kristaps Porzingis', 'Giannis Antetokounmpo':'Grayson Allen',
'Kevin Durant':'James Harden', 'Steph Curry':'Kevin Durant', 'Donavan Mitchell':'Jordan Clarkson','Devin Booker': 'DeAndre Ayton',
'Trae Young':'Vince Carter' , 'Nikola Jokic':'Mason Plumlee', 'Damian Lillard':'Carmelo Anthony', 'Lebron James':'Kyrie Irving','Kevin Garnett':'Rajan Rondo',
'Russell Westbrook':'Serge Ibaka','Anthony Edwards':'D\'Angelo Russell','DeMar DeRozan':'Zach LaVine','Paul George':'PJ Dozier','Pascal Siakam':'Kawhi Leonard',
'Julius Randle':'Kobe Bryant'


}




players = ['Joel Embiid', 'Luka Doncic', 'Giannis Antetokounmpo', 'Kevin Durant', 'Steph Curry', 'Donavan Mitchell','Devin Booker', 'Trae Young' , 'Nikola Jokic', 'Damian Lillard', 'Lebron James', 'Kevin Garnett','Russell Westbrook','Anthony Edwards','DeMar Derozan','Paul George','Pascal Siakam','Julius Randle']
college = ['Kansas','Spain','Greece', 'Texas','Davidson','Louisville', 'Kentucky','Oklahoma', 'Serbia', 'Weber State', 'High School','High School','UCLA','Georgia','USC', 'Fresno State','New Mexico State','Kentucky']
position = ['Center','Guard','Forward','Forward','Guard','Guard','Guard','Guard','Center','Guard','Forward','Forward','Guard','Guard','Forward','Forward','Forward','Forward']
career_high = ['70','73','64','55','62','71','70','56','53','70','61','47','58','49','52','48','44','57']
random_number = random.randint(0,len(players) - 1)
random_player = players[random_number]
random_college = college[random_number]
random_position = position[random_number]
teamate = player_teamate.get(random_player)
player_high = career_high[random_number]
#print (teamate)


print("This player used to play with " + teamate + '.')
check(random_college,random_position,teamate,random_player,x)





























