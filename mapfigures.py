#tokens
# pk.eyJ1IjoibGVnYWxiZWFyaGsiLCJhIjoiY2s2M21hdjZ4MHFzZDNlb2ZrMXZqMWRpbyJ9.AULfgQRbnvJFom3GPfzEbg
#mapbox://styles/legalbearhk/ck63n0ccp0uun1is2giqghm0i
import pandas as pd
import plotly.graph_objects as go

mapbox_access_token = "pk.eyJ1IjoibGVnYWxiZWFyaGsiLCJhIjoiY2s2M21hdjZ4MHFzZDNlb2ZrMXZqMWRpbyJ9.AULfgQRbnvJFom3GPfzEbg"

df = pd.read_csv("data/map_data.csv")
site_lat = df.Lat
site_lon = df.Lon
locations_name = [i for i in df.地點]
lastAppearDate = [i for i in df.最後曾逗留日期]
hoverstringg = [i+" <br>最後曾逗留日期:" +q for i,q in zip(locations_name, lastAppearDate)]


fig = go.Figure()

fig.add_trace(go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        #text=locations_name,
        hoverinfo='none',
    ))

fig.add_trace(go.Scattermapbox(

        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=8,
            color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        hoverinfo='text',
        #hovertemplate = "  %{labels} Date: %{text}"
        text=hoverstringg,
    ))

fig.update_layout(
    title='受感染病人住所',
    autosize=True,
    #width= 800,
    height = 800,
    hovermode='closest',
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        zoom=10,
        bearing= 0,
        center=go.layout.mapbox.Center(
            lat= 22.345837,
            lon= 114.173204
        ),
        pitch=0,
        style='dark'
    ),
)
