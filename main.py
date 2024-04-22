from bokeh.plotting import figure 
from bokeh.io import export_png
import pandas as pd

def generate_plots(sheet_name, df):
    TP1_list = df['TP1'].tolist()
    TP2_list = df['TP2'].tolist()
    time_list = df.iloc[:, 0].tolist()
    diff_list = df['Diff'].tolist()

    TP1_graph = figure(title="TP1 graph", x_axis_label='Time', y_axis_label='TP1')
    TP1_graph.line(time_list, TP1_list, line_width=5)
    export_png(TP1_graph, filename=f'graphs/TP1 {sheet_name}.png')

    TP2_graph = figure(title="TP2 graph", x_axis_label='Time', y_axis_label='TP2')
    TP2_graph.line(time_list, TP2_list, line_width=5)
    export_png(TP2_graph, filename=f'graphs/TP2 {sheet_name}.png')

    diff_graph = figure(title="Diff graph", x_axis_label='Time', y_axis_label='Diff')
    diff_graph.line(time_list, diff_list, line_width=5)
    export_png(diff_graph, filename=f'graphs/diff {sheet_name}.png')
    
    print(f'sheet {sheet_name} done!')

def main():
    for sheets in range(1, 6):
        sheet_name = f'run-{sheets}'    
        
        df = pd.read_excel('run-data_raw.xlsx', sheet_name=sheet_name)

        generate_plots(sheet_name, df)


if __name__ == '__main__':
    main()
