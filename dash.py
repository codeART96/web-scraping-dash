import dash
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash()

# Creating DATA

df = pd.read_csv('epl_stats_2.csv')
labels = df.team
app.layout = html.Div([
         dcc.Markdown('''
#### The stats for EPL teams through the 2019/2020 Season. 
The purpose of the Dashboard is to see which features have the biggest impact on a team winning the League.
The goal difference of teams which have won the league have been less than 10 before such as Leicester City in 2016/2017 season,
 the number of points for second place was made by Liverpool in 2018/2019 season, the numbers of losses it takes to get relegated is determined
 on the league as a whole. With this is information i would like to predict teams which have a chance of winning the league,
by adding more features, this coould help staticians and bookies to calculate the odds.
'''),
         
         dcc.Graph(id='scatterplot',
                    figure = {'data':[
                            go.Scatter(
                            x=df.team,
                            y=df.attendance,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='Attendance of EPL Teams',
                                        yaxis = {'title':'Attendance'})}
                    ),
dcc.Markdown('''
#### The stadium maximum attendance. 
The number of home supporters have a influence on how a team performs, I wanted to investigated if teams with the least attendance
have a impact in the top ten in top flight football.
'''),

                   

                    dcc.Graph(id='scatterplot2',
                    figure = {'data':[
                            go.Scatter(
                            x=df.team,
                            y=df.goal_diff,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='Goal Difference',
                                        yaxis = {'title':'Goal Difference'})}
                    ),

dcc.Markdown('''
#### The Goal Difference. 
The goal difference shows how teams are performing, a low goal difference, shows that a team is scoring as much as they are conceding,
or in some cases, might not be conceding goals and winning with low tallies. Negative goal difference, means the team is conceding more goals
than their are scoring, therefore there is high chance they in a relagation zone. 
'''),

        dcc.Graph(id='Bar',
                     figure = {'data':[
                            go.Bar(
                            x=df.team,
                            y=df.wins,
                            name='wins',
                            ),
                            go.Bar(
                            x=df.team,
                            y=df.losses,
                            name='losses',
                            ),
                            go.Bar(
                            x=df.team,
                            y=df.draws,
                            name='Draws',
                            )
                     
                            
                            ],
                    'layout':go.Layout(title='Wins,Losses & Draws per team',
                                        yaxis = {'title':'Stats'})}
                    ),
                    
 dcc.Markdown('''
#### The Wins, Draws,Losses. 
In order for a team to win a league, they would have to win the most games or lose the least, by drawing games a team loses 2 points and
gains 1, by winning they recieve 3 points. Teams can go a season without losing and still not win the league becuase of draws, these features
are important when checking for winning the league of relgation status.
'''),
   
                    dcc.Graph(id='pie',
                                        figure = {'data':[
                                                go.Pie(
                                                values = df.wins,
                                                labels= df.team
                                                )],
                                        'layout':go.Layout(title='Wins percentage of Team',
                                         yaxis = {'title':'Wins'})}
                                        )])

                       
                   

if __name__ == '__main__':
    app.run_server(debug=True)