import pandas as pd
import matplotlib.pyplot as plt


#Just to get data to debug and check stuff
def filter(id, variable,df):                                                       
    tmp=df                                                                      
    if(id):                                                                     
        tmp = tmp[tmp['id'] == id]                                              
    if(variable):                                                               
        tmp = tmp[tmp['variable'] == variable]                                  
    return tmp  

#returns the two dataset, mood data and the other variables in a matrix variable/values
def get_data(df):
    #drop rows with unvalid timestamps
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    df = df.dropna(subset=['time'])

    mood_data = df[df['variable'] == 'mood']
    other_variables_data = df[df['variable'] != 'mood']



    # A matrix containing all the different variable and their values
    variable_data = {}
    for variable in other_variables_data['variable'].unique():
        variable_data[variable] = other_variables_data[other_variables_data['variable'] == variable]

    return mood_data, variable_data

# Plots stuff
def plot(mood, mood_points, others, others_points):
    for variable, data in others.items():
        #fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig, axes = plt.subplots(figsize=(10, 6))

        # Scatter Plot
        mood_data = mood.iloc[:mood_points]
        axes.plot(mood_data['time'], mood_data['value'], marker='o', linestyle='-', label='Mood')
        data_sorted = data.sort_values(by='time').iloc[:others_points]
        axes.plot(data_sorted['time'], data_sorted['value'], marker='o', linestyle='-', label=variable)
        axes.set_title(f'Scatter Plot: {variable} vs Mood (First {others_points} Points, Sorted by Timestamp)')
        axes.set_xlabel('Time')
        axes.set_ylabel('Value')
        axes.legend()
        axes.grid(True)
        axes.tick_params(axis='x', rotation=45)

        #useless, they look like shit
        '''
        # Bar Plot
        axes[0, 1].plot(mood_data['time'], mood_data['value'], marker='o', linestyle='-', label='Mood')
        axes[0, 1].bar(data_sorted['time'], data_sorted['value'], label=variable, alpha=0.7)
        axes[0, 1].set_title(f'Bar Plot: {variable} vs Mood (First {others_points} Points, Sorted by Timestamp)')
        axes[0, 1].set_xlabel('Time')
        axes[0, 1].set_ylabel('Value')
        axes[0, 1].legend()
        axes[0, 1].grid(True)
        axes[0, 1].tick_params(axis='x', rotation=45)

        # Box Plot
        axes[1, 0].boxplot(data_sorted['value'], patch_artist=True)
        axes[1, 0].set_title(f'Box Plot: {variable} Distribution')
        axes[1, 0].set_ylabel('Value')
        axes[1, 0].grid(True)

        # Heatmap
        numerical_data = data_sorted.select_dtypes(include=['float', 'int'])
        correlation_matrix = numerical_data.corr()
        heatmap = axes[1, 1].imshow(correlation_matrix, cmap='coolwarm')
        fig.colorbar(heatmap, ax=axes[1, 1])
        axes[1, 1].set_title(f'Correlation Heatmap: {variable}')
        axes[1, 1].set_xticks(range(len(correlation_matrix.columns)))
        axes[1, 1].set_yticks(range(len(correlation_matrix.columns)))
        axes[1, 1].set_xticklabels(correlation_matrix.columns)
        axes[1, 1].set_yticklabels(correlation_matrix.columns)
        '''
        
        plt.tight_layout()
        plt.show()



#I like stuff well formatted dont judge me.
def print_info(mood, others):
    max_var_length = max(len("Variable Name"), max(len(variable) for variable in others.keys()))
    max_first_ts_length = max(len("First Timestamp"), max(len(data['time'].iloc[0].strftime('%Y-%m-%d %H:%M:%S')) for data in others.values()))
    max_last_ts_length = max(len("Last Timestamp"), max(len(data['time'].iloc[-1].strftime('%Y-%m-%d %H:%M:%S')) for data in others.values()))

    # Print table header
    print("Variable Name".ljust(max_var_length), "Number of Points".ljust(18), "First Timestamp".ljust(max_first_ts_length), "Last Timestamp".ljust(max_last_ts_length))
    print("-" * (max_var_length + 18 + max_first_ts_length + max_last_ts_length))

    # Print data rows
    print(f"Mood".ljust(max_var_length), f"{len(mood)}".ljust(18), f"{mood['time'].iloc[0].strftime('%Y-%m-%d %H:%M:%S')}".ljust(max_first_ts_length), f"{mood['time'].iloc[-1].strftime('%Y-%m-%d %H:%M:%S')}".ljust(max_last_ts_length))
    for variable, data in others.items():
        print(variable.ljust(max_var_length), f"{len(data)}".ljust(18), f"{data['time'].iloc[0].strftime('%Y-%m-%d %H:%M:%S')}".ljust(max_first_ts_length), f"{data['time'].iloc[-1].strftime('%Y-%m-%d %H:%M:%S')}".ljust(max_last_ts_length))

    '''
    Variable Name        Number of Points   First Timestamp     Last Timestamp     
    ----------------------------------------------------------------------------
    Mood                 5641               2014-02-26 13:00:00 2014-05-31 12:00:00
    circumplex.arousal   5643               2014-02-26 13:00:00 2014-05-31 12:00:00
    circumplex.valence   5643               2014-02-26 13:00:00 2014-05-31 12:00:00
    activity             22965              2014-03-20 22:00:00 2014-05-30 22:00:00
    screen               96578              2014-03-20 23:14:58 2014-05-30 22:18:11
    call                 5239               2014-02-17 12:04:42 2014-05-30 15:52:26
    sms                  1798               2014-02-19 17:42:34 2014-05-29 23:07:30
    appCat.builtin       91288              2014-03-20 22:25:56 2014-05-30 22:32:15
    appCat.communication 74276              2014-03-20 22:25:58 2014-05-30 22:31:07
    appCat.entertainment 27125              2014-03-20 22:40:30 2014-05-30 21:50:08
    appCat.finance       939                2014-03-21 10:26:32 2014-04-28 12:53:34
    appCat.game          813                2014-03-28 18:30:14 2014-05-03 18:38:57
    appCat.office        5642               2014-03-21 11:17:02 2014-05-28 16:27:20
    appCat.other         7650               2014-03-20 22:25:45 2014-05-30 20:59:22
    appCat.social        19145              2014-03-20 22:49:38 2014-05-30 22:06:07
    appCat.travel        2846               2014-03-21 10:39:42 2014-05-30 16:21:59
    appCat.unknown       939                2014-03-20 23:33:38 2014-05-30 13:20:54
    appCat.utilities     2487               2014-03-20 23:22:49 2014-05-30 22:32:05
    appCat.weather       255                2014-03-23 16:21:32 2014-04-07 18:25:14
    '''

def main():
    df = pd.read_csv('dataset/mood_dataset.csv')

    mood, others = get_data(df)
    print_info(mood, others)
    
    # mood_points is our base and comparing_points are the points of the other variable we checking
    mood_points = 100
    others_points = 10
    plot(mood,mood_points, others, others_points)

   

if __name__ == "__main__":
    main()