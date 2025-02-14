from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from _thread import start_new_thread

class MenuScreen(Screen):
    pass
class MostRuns(Screen):
    pass
class MostSixes(Screen):
    pass
class MostFours(Screen):
    pass
class HighestIndividualScore(Screen):
    pass
class HighestBattingStrikeRate(Screen):
    pass
class MostWicketTaker(Screen):
    pass
class BestBowlingAverage(Screen):
    pass
class BestBowlingEconomy(Screen):
    pass
class BestBowlingFigure(Screen):
    pass
class MostDotBalls(Screen):
    pass



class FirstappApp(MDApp):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MostRuns(name='runs'))
        sm.add_widget(MostSixes(name='sixes'))
        sm.add_widget(MostFours(name='fours'))
        sm.add_widget(HighestIndividualScore(name='high score'))
        sm.add_widget(HighestBattingStrikeRate(name='strike rate'))
        sm.add_widget(MostWicketTaker(name='wickets'))
        sm.add_widget(BestBowlingAverage(name='average'))
        sm.add_widget(BestBowlingEconomy(name='economy'))
        sm.add_widget(BestBowlingFigure(name='figure'))
        sm.add_widget(MostDotBalls(name='dot balls'))
        return sm

app=FirstappApp()
app.run()


run = [5878,5368,5254,5230,5197,4849,4772,4632,4607,4217]
# def most_runs():
#     print("----------------------------------")
#     print('Most Runs')
#     print("----------------------------------")
#     print('1.Virat Kohli :', run[1], 'Runs')
#     print('2.Suresh Raina :', run[2], 'Runs')
#     print('3.David Warner :', run[3], 'Runs')
#     print('4.Rohit Sharma :', run[4], 'Runs')
#     print('5.Shikhar Dhawan :', run[5], 'Runs')
#     print('6.AB de Villiers :', run[6], 'Runs')
#     print('7.Chris Gayle :', run[7], 'Runs')
#     print('8.MS Dhoni :', run[8], 'Runs')
#     print('9.Robin Uthappa :', run[9], 'Runs')
#     print('10.Gautam Gambhir :', run[10], 'Runs')
#     print("Press 0 For Menu")



six = [0,349,235,216,213,201,198,195,194,190,163]
def most_six():
    print("----------------------------------")
    print('Most Six')
    print("----------------------------------")
    print('1.Chris Gayle :', six[1], 'Sixes')
    print('2.AB de Villiers :', six[2], 'Sixes')
    print('3.MS Dhoni :', six[3], 'Sixes')
    print('4.Rohit Sharma :', six[4], 'Sixes')
    print('5.Virat Kohli :', six[5], 'Sixes')
    print('6.Kieron Pollard :', six[6], 'Sixes')
    print('7.David Warner :', six[7], 'Sixes')
    print('8.Suresh Raina :', six[8], 'Sixes')
    print('9.Shane Watson :', six[9], 'Sixes')
    print('10.Robin Uthappa :', six[10], 'Sixes')
    print("Press 0 For Menu")



fr = [0,591,510,503,493,491,458,454,416,390,384]
def most_four():
    print("----------------------------------")
    print('Most Fours')
    print("----------------------------------")
    print('1.Shikhar Dhawan :', fr[1], 'Fours')
    print('2.David Warner :', fr[2], 'Fours')
    print('3.Virat Kohli :', fr[3], 'Fours')
    print('4.Suresh Raina :', fr[4], 'Fours')
    print('5.Gautam Gambhir :', fr[5], 'Fours')
    print('6.Rohit Sharma :', fr[6], 'Fours')
    print('7.Robin Uthappa :', fr[7], 'Fours')
    print('8.Ajinkya Rahane :', fr[8], 'Fours')
    print('9.AB de Villiers :', fr[9], 'Fours')
    print('10.Chris Gayle :', fr[10], 'Fours')
    print("Press 0 For Menu")



hs = [0,175,158,133,132,129,128,128,127,126,122]
def highest_score():
    print("----------------------------------")
    print('Highest Individual Score')
    print("----------------------------------")
    print('1.Chris Gayle  :', hs[1], 'Runs')
    print('2.Brendon mcCullum  :', hs[2], 'Runs')
    print('3.AB de Villiers  :', hs[3], 'Runs')
    print('4.KL Rahul  :', hs[4], 'Runs')
    print('5.AB de Villiers  :', hs[5], 'Runs')
    print('6.Chris Gayle  :', hs[6], 'Runs')
    print('7.Rishabh Pant  :', hs[7], 'Runs')
    print('8.Murali Vijay  :', hs[8], 'Runs')
    print('9.David Warner  :', hs[9], 'Runs')
    print('10.Virender Sehwag  :', hs[10], 'Runs')
    print("Press 0 For Menu")


sr = [0,182.33,165.39,164.27,159.26,158.46,157.87,155.44,154.67,151.97,151.91]
def strike_rate():
    print("----------------------------------")
    print('Highest Batting Strike Rate')
    print("----------------------------------")
    print('1.Andre Russel :', sr[1], 'R/B')
    print('2.Nicholas Pooran :', sr[2], 'R/B')
    print('3.Sunil Narine :', sr[3], 'R/B')
    print('4.Hardik Pandya :', sr[4], 'R/B')
    print('5.Moeen Ali :', sr[5], 'R/B')
    print('6.Chriss Morris :', sr[6], 'R/B')
    print('7.Virender Sehwag :', sr[7], 'R/B')
    print('8.Glenn Maxwell :', sr[8], 'R/B')
    print('9.Rishabh Pant :', sr[9], 'R/B')
    print('10.AB de Villiers :', sr[10], 'R/B')
    print("Press 0 For Menu")



wkt = [0,170,160,156,153,150,138,136,127,121,119]
def wicket():
    print("----------------------------------")
    print('Most Wickets')
    print("----------------------------------")
    print('1.Lasith Malinga :', wkt[1], 'wickets')
    print('2.Amit Mishra :', wkt[2], 'wickets')
    print('3.Piyush Chawla :', wkt[3], 'wickets')
    print('4.Dwayne Bravo :', wkt[4], 'wickets')
    print('5.Harbhajan Singh :', wkt[5], 'wickets')
    print('6.R Ashwin :', wkt[6], 'wickets')
    print('7.B Kumar :', wkt[7], 'wickets')
    print('8.Sunil Narine :', wkt[8], 'wickets')
    print('9.Y Chahal :', wkt[9], 'wickets')
    print('10.Umesh Yadav :', wkt[10], 'wickets')
    print("Press 0 For Menu")



avg = [0,18.09,18.72,18.73,19.25,19.80,20.38,20.49,21.00,21.00,21.08]
def average():
    print("----------------------------------")
    print('Best Bowling Average')
    print("----------------------------------")
    print('1.Kagiso Rabada :', avg[1], 'R/W')
    print('2.Doug Bollinger :', avg[2], 'R/W')
    print('3.Dimitri Mascarenhas :', avg[3], 'R/W')
    print('4.MF Mahroof :', avg[4], 'R/W')
    print('5.Lasith Malinga :', avg[5], 'R/W')
    print('6.Mitchell Starc :', avg[6], 'R/W')
    print('7.Rashid Khan :', avg[7], 'R/W')
    print('8.Mitchell Marsh  :', avg[8], 'R/W')
    print('9.Khaleel Ahmed :', avg[9], 'R/W')
    print('10.Imran Tahir :', avg[10], 'R/W')
    print("Press 0 For Menu")

eco = [0,6.24,6.57,6.61,6.67,6.74,6.77,6.78,6.87,6.87,6.91]
def economy():
    print("----------------------------------")
    print('Best Bowling Economy')
    print("----------------------------------")
    print('1.Rashid Khan :', eco[1], 'R/O')
    print('2.Anil Kumble :', eco[2], 'R/O')
    print('3.Glenn Maxwell  :', eco[3], 'R/O')
    print('4.M Muralidharan :', eco[4], 'R/O')
    print('5.Roelof Merwe :', eco[5], 'R/O')
    print('6.Sunil Narine :', eco[6], 'R/O')
    print('7.Daniel Vittori :', eco[7], 'R/O')
    print('8.W Sundar :', eco[8], 'R/O')
    print('9.R Ashwin :', eco[9], 'R/O')
    print('10.Dale Steyn :', eco[10], 'R/O')
    print("Press 0 For Menu")



bf = [0,6,6,6,5,5,5,5,5,5,5,12,14,19,5,12,13,14,16,16,17]
def bow_fig():
    print("----------------------------------")
    print('Best Bowling Figures')
    print("----------------------------------")
    print('1.Alzarri Joseph :', bf[1], '/' ,bf[11])
    print('2.Sohail Tanveer :', bf[2], '/' ,bf[12])
    print('3.Adam Zampa :', bf[3], '/' ,bf[13])
    print('4.Anil Kumble :', bf[4], '/' ,bf[14])
    print('5.Ishant Sharma :', bf[5], '/' ,bf[15])
    print('6.Lasith Malinga :', bf[6], '/' ,bf[16])
    print('7.Ankit Rajpoot :', bf[7], '/' ,bf[17])
    print('8.James Faulkner :', bf[8], '/' ,bf[18])
    print('9.Ravindra Jadeja :', bf[9], '/' ,bf[19])
    print('10.Amit Mishra :', bf[10], '/' ,bf[20])
    print("Press 0 For Menu")


db = [0,1249,1170,1164,1155,1146,1129,1118,1076,1022,962]
def dot_balls():
    print("----------------------------------")
    print('Most Dot Balls')
    print("----------------------------------")
    print('1.Harbhajan Singh :', db[1], ' Dot balls')
    print('1.Harbhajan Singh :', db[1], ' Dot balls')
    print('2.R Ashwin :', db[2], ' Dot balls')
    print('3.B Kumar :', db[3], ' Dot balls')
    print('4.Lasith Malinga :', db[4], ' Dot balls')
    print('5.Piyush Chawla :', db[5], ' Dot balls')
    print('6.Amit Mishra :', db[6], ' Dot balls')
    print('7.Sunil Narine :', db[7], ' Dot balls')
    print('8.Praveen Kumar :', db[8], ' Dot balls')
    print('9.Dale Steyn :', db[9], ' Dot balls')
    print('10.Umesh Yadav :', db[10], ' Dot balls')
    print("Press 0 For Menu")

def menu():
    print("Welcome To IPL All Time Statistics")
    print("----------------------------------")
    print("1)Most Runs")
    print("2)Most Six")
    print("3)Most Fours")
    print("4)Highest Individual Score")
    print("5)Highest Batting Srike Rate")
    print("6)Most Wicket Taker")
    print("7)Best Bowling Average")
    print("8)Best Bowling Economy")
    print("9)Best Bowling Figure")
    print("10)Most Dot Balls")
    print("11)Exit")
    print("----------------------------------")
    print("Enter your choice")
