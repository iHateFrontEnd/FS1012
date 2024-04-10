from matplotlib import pyplot as plt
import pandas as pd

def main():

    for sheets in range(1, 6):
        sheet_name = f'run {sheets}'    
        
        df = pd.read_excel('run-data_raw.xlsx', sheet_name=sheet_name)

        columns = ['Time', 'TP1', 'TP2', 'Diff']

        df = df[columns]

        TP1_list = []
        TP2_list = []
        time_list = []
        diff_list = []

        for i in df.Time:
            time_list.append(i)

        for i in df.TP1:
            TP1_list.append(i)
        
        for i in df.TP2:
            TP2_list.append(i)
        
        for i in df.Diff:
            diff_list.append(i)

        plt.title(f'TP1 {sheet_name}')
        plt.plot(time_list, TP1_list)
        plt.xlabel('Time')
        plt.ylabel('TP1')
        plt.savefig(f'graphs/TP1 {sheet_name}.png')
        plt.clf()

        plt.title(f'TP2 {sheet_name}')
        plt.plot(time_list, TP2_list)
        plt.xlabel('Time')
        plt.ylabel('TP2')
        plt.savefig(f'graphs/TP2 {sheet_name}.png')
        plt.clf()

        plt.title(f'Diff {sheet_name}')
        plt.plot(time_list, diff_list)
        plt.xlabel('Time')
        plt.ylabel('Diff')
        plt.savefig(f'graphs/diff {sheet_name}.png')
        plt.clf()

        print(f'sheet {sheet_name} done!')

if __name__ == '__main__':
    main()
