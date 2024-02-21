from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure, show, output_file
from motion_detector import df

# add the dates and time in better format onto df to be displayed by the hovertool later
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d-%H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d-%H:%M:%S")

cds = ColumnDataSource(df)

f = figure(x_axis_type='datetime', height=150, width=800, title="Motion Graph")
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker.desired_num_ticks = 1

#Add a hover tool that displays date and time
hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)

p = f.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

#Convert the plot to html
output_file("motion_graph.html")
show(f)
