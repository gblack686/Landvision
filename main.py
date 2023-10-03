from bokeh.models import TabPanel, Tabs
from bokeh.plotting import figure, show, curdoc
import pandas as pd
from tabs import scattergraph_floorplans_tab

floorplans = pd.read_csv('./landvision/data/floorplans.csv')
scatplot = scattergraph_floorplans_tab.scattergraph_tab(floorplans)
print(type(scatplot))

# Create a tab for the plot

# p1 = figure(width=300, height=300)
# p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
# tab1 = TabPanel(child=scatplot, title="Competitive Market Analysis")

# show(Tabs(tabs=[scatplot]))

curdoc().add_root(Tabs(tabs=[scatplot],name='tabs'))    
# curdoc().template_variables["tabs"] = Tabs(tabs=[scatplot])

