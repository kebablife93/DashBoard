import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import dash
import dash_html_components as html
import plotly.graph_objects as go
import plotly
import plotly.graph_objects as go




covid = pd.read_csv("covid.csv")

# Création de la carte

carte1 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",
                        hover_data=["Country","Date", "Confirmed","Recovered", "Deaths", "Active"],
                        color="Confirmed", zoom=2, height=800,color_continuous_scale='Inferno',
                        title="Répartition des cas confirmés dans le monde")
carte1.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Données COVID-19 dans le monde ",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],
    title_x=0.5,
    title_y=0.98,
    titlefont={ "size": 35, "color":'#1C2840' }

      )
carte1.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})



carte2 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",
                        hover_data=["Country","Date", "Confirmed","Recovered", "Deaths", "Active"],
                        size="Confirmed",color="Confirmed", zoom=2, height=800,color_continuous_scale='Inferno',
                        title="Répartition des cas confirmés dans le monde")
carte2.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Données COVID-19 dans le monde ",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],
    title_x=0.5,
    title_y=0.98,
    titlefont={ "size": 35, "color":'#1C2840' }

      )
carte2.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})
# Création des Graphiques

#Création du graphe en frommage

#Organisation des données pour n'avoir aucune donnée nulle pour faire le pourcentage
confirm=covid.loc[covid['Confirmed']>0].count()[0]
dead=covid.loc[covid['Deaths']>0].count()[0]
recov=covid.loc[covid['Recovered']>0].count()[0]
active=covid.loc[covid['Active']>0].count()[0]


#Définition des différentes parties du frommage

labels=['Mort','Soigné','Actif']
values = [dead,recov,active]


#Couleurs des différentes parties du frommage

colors = ['#384b7e', '#122425', '#223565']

#Création du graphique 

cheese = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                        marker_colors=colors, hole=.1,
                        insidetextorientation='radial',textfont_size=25
                            )])

#Ajout d'une couleur de fond au graphique, taille, titre
cheese.layout.paper_bgcolor = '#AD94A6'
cheese.update_layout(title_text="Répartition du type des cas confirmés",titlefont={ "size": 35, "color":"#FFFFFF" },hoverlabel={"bgcolor":"white","font_size":30,"font_family":"Rockwell"})


#Création de l'histogramme représentant les cas du Covid confirmés en fonction de la date 

figure1 = px.histogram(covid, x="Date",y="Confirmed", color="Country",title='Évolution des cas confirmés dans le temps',template='plotly_dark')
figure1.update_layout(titlefont={ "size": 25 })


#Création du graphique représentant le nombre de morts par pays

figure2 = px.scatter(covid, x="Country", y="Deaths", title='Nombre de morts par pays',template='plotly_dark', color="Country")
figure1.update_layout(titlefont={ "size": 25 })


#Création du graphique représentant le nombre de morts par pays en fonction du temps

figure3 = px.scatter(covid, x="Date", y="Deaths", color="Country", title="Nombre de morts par pays en fonction du temps",template='plotly_dark')
figure3.update_layout(titlefont={ "size": 25 })


#Création du graphique représentant le nombre de cas confirmé par pays en fonction du temps

figure4 = px.histogram(covid, x="Confirmed",y="Deaths", color="Country",title='Nombre de morts en fonction des cas confirmé',template='plotly_dark')
figure4.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts en fonction des cas confirmé

figure5 = px.scatter(covid, x="Date", y="Confirmed", color="Country",title='Nombre de cas confirmé par pays en fonction du temps',template='plotly_dark')
figure5.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant l'évolution du nombre de morts par pays dans le temps

figure6 = px.bar(covid,x="Country",y="Confirmed",title='Évolution du nombre de morts par pays dans le temps',animation_group="Country",animation_frame="Date",range_y=[0,14000000], height=800,template='plotly_dark')
figure6.update_layout(titlefont={ "size": 25 })

figure6.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5
figure6.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

# Création du DASHBOARD

app = dash.Dash(__name__) # Créer le dashboard
# Générer le code HTML
app.layout = html.Div(style={'background-color':'#1C2840'},children=[

                        html.H1("Données COVID-19 dans le monde", style={'text-align': 'center', 'color':'white', 'padding-top':'2vh','padding-bottom':'2vh'}),

                        html.Br(),
                        #Dessin de l'élément dans le dashboard
                        dcc.Graph(
                            id='Carte1',
                            figure=carte1
                            ),
                        dcc.Graph(
                            id='Carte2',
                            figure=carte2
                            ),
                        #Graphiques
                        dcc.Graph(
                            id='graph2',
                            figure=figure1
                            ),
                        dcc.Graph(
                            id='graph3',
                            figure=figure2
                            ),
                        dcc.Graph(
                            id='graph4',
                            figure=figure3
                            ),
                        dcc.Graph(
                            id='graph5',
                            figure=figure4
                            ),
                        dcc.Graph(
                            id='graph6',
                            figure=figure5
                            ), 
                        dcc.Graph(
                            id='graph7',
                            figure=figure6
                            ), 
                        dcc.Graph(
                            id='graph8',
                            figure=cheese,
                            style={'height': '90vh', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
                            ), 
])        
        
# Lance le Dashboard

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    
    
    