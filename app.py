from flask import Flask, render_template
import pandas as pd
from pandas_highcharts.core import serialize
from pandas.compat import StringIO

app = Flask(__name__)

dat = """ts;A;B;C
2015-01-01 00:00:00;27451873;29956800;113
2015-01-01 01:00:00;20259882;17906600;76
2015-01-01 02:00:00;11592256;12311600;48
2015-01-01 03:00:00;11795562;11750100;50
2015-01-01 04:00:00;9396718;10203900;43
2015-01-01 05:00:00;14902826;14341100;53"""

@app.route('/')
def main():
	df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates=['ts'])
	# Basic line plot
	chart1 = serialize(df, render_to="my-chart1", title="My Chart")
	# Basic column plot
	chart2 = serialize(df, render_to="my-chart2", title="Test", kind="bar")
	# Basic column plot
	chart3 = serialize(df, render_to="my-chart3", title="Test", kind="barh")
	# Plot C on secondary axis
	chart4 = serialize(df, render_to="my-chart4", title="Test", secondary_y = ["C"])
	# Plot on a 1000x700 div
	chart5 = serialize(df, render_to="my-chart5", title="Test", figsize = (1000, 700))
	return render_template('index.html', chart1=chart1, chart2=chart2, chart3=chart3,
		chart4=chart4, chart5=chart5)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)