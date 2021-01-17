import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import dash
import dash_html_components as html
import plotly.graph_objects as go
import plotly
import plotly.graph_objects as go




covid = pd.read_csv("covid.csv")



#########################################################################################################################################################################################################################################

# Création de la 1ère carte

carte1 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",
                        hover_data=["Country","Date", "Confirmed","Recovered", "Deaths", "Active"],
                        color="Confirmed",size="Confirmed", zoom=2, height=800,color_continuous_scale=px.colors.sequential.Inferno,
                        title="Répartition des cas confirmés dans le monde")
carte1.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Répartition des cas confirmés dans le monde",
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

# Création de la 2ème carte
carte2 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",
                        hover_data=["Country","Date","Deaths"],
                        color_discrete_sequence=["red"], zoom=2, height=800,

                        title="Répartition des cas morts dans le monde")
carte2.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Répartition des cas morts dans le monde",
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

#Création du graphique frommage 

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

#Création de l'histogramme représentant les morts du Covid confirmés en fonction de la date 

figure2 = px.histogram(covid, x="Date",y="Deaths",color="Country",title='Évolution des cas décédés dans le temps',template='plotly_dark')
figure2.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de cas confirmé par pays

figure3 = px.scatter(covid, x="Country", y="Confirmed", color="Country", title="Nombre de cas confirmé par pays",template='plotly_dark')
figure3.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts par pays

figure4 = px.scatter(covid, x="Country", y="Deaths", title='Nombre de morts par pays',template='plotly_dark', color="Country")
figure4.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de cas confirmé par pays en fonction du temps

figure5 = px.scatter(covid, x="Date", y="Confirmed", color="Country",title='Nombre de cas confirmé par pays en fonction du temps',template='plotly_dark')
figure5.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts par pays en fonction du temps

figure6 = px.scatter(covid, x="Date", y="Deaths", color="Country", title="Nombre de morts par pays en fonction du temps",template='plotly_dark')
figure6.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant l'évolution du nombre de morts par pays dans le temps

figure7 = px.bar(covid,x="Country",y="Confirmed",title='Évolution du nombre de morts par pays dans le temps',animation_group="Country",animation_frame="Date",range_y=[0,14000000], height=800,template='plotly_dark')
figure7.update_layout(titlefont={ "size": 25 })

figure7.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5
figure7.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

#Création du graphique représentant le nombre de morts en fonction des cas confirmés

figure8 = px.histogram(covid, x="Confirmed",y="Deaths", color="Country",title='Nombre de morts en fonction des cas confirmés',template='plotly_dark')
figure8.update_layout(titlefont={ "size": 25 })

#########################################################################################################################################################################################################################################


# Création du DASHBOARD

app = dash.Dash(__name__) # Créer le dashboard
# Générer le code HTML
app.layout = html.Div(style={'background-color':'#1C2840'},children=[

                        html.H1("Données COVID-19 dans le monde", style={'text-align': 'center', 'color':'white', 'padding-top':'2vh','padding-bottom':'2vh'}),

                        html.Br(),
                        #Dessin de l'élément dans le dashboard

                        #Création de la carte des répartitions des cas confirmés dans le monde
                        dcc.Graph(
                            id='Carte1',
                            figure=carte1
                            ),
                        #Création de la carte des répartitions des cas morts dans le monde
                        dcc.Graph(
                            id='Carte2',
                            figure=carte2
                            ),

                        #Graphiques

                        #Création de l'histogramme représentant les cas du Covid confirmés en fonction de la date 
                        dcc.Graph(
                            id='graph1',
                            figure=figure1
                            ),
                        #Création de l'histogramme représentant les morts du Covid confirmés en fonction de la date 
                        dcc.Graph(
                            id='graph2',
                            figure=figure2
                            ),
                        #Création du graphique représentant le nombre de cas confirmé par pays
                        dcc.Graph(
                            id='graph3',
                            figure=figure3
                            ), 
                        #Création du graphique représentant le nombre de morts par pays
                        dcc.Graph(
                            id='graph4',
                            figure=figure4
                            ),   
                        #Création du graphique représentant le nombre de cas confirmé par pays en fonction du temps
                        dcc.Graph(
                            id='graph5',
                            figure=figure5
                            ),   
                        #Création du graphique représentant le nombre de morts par pays en fonction du temps
                        dcc.Graph(
                            id='graph6',
                            figure=figure6
                            ),
                        #Création du graphique représentant l'évolution du nombre de morts par pays dans le temps                                                    
                        dcc.Graph(
                            id='graph7',
                            figure=figure7
                            ),
                        #Création du graphique représentant le nombre de morts en fonction des cas confirmés
                        dcc.Graph(
                            id='graph8',
                            figure=figure8
                            ),
                        #Création du graphique frommage 
                        dcc.Graph(
                            id='cheese',
                            figure=cheese,
                            style={'height': '90vh', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
                            )
])        
        

#########################################################################################################################################################################################################################################

# Lance le Dashboard

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    
    
    