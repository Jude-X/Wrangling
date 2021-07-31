#import pandas module for data wrangling
import pandas as pd

def get_csv(url):
    '''
    This function scraps a wikipedia page for table and returns a csv file
    The column headers of this csv file are: 
    Country, Year, Area, Population, GDP per capita, Population density, 
    Vehicle ownership, Total road deaths, and Road deaths per Million Inhabitants.
    '''
    ## Read Html from url
    df = pd.read_html(url)
    
    ## Select the table with an index of its position
    df = df[2]
    
    #Edit column names to match requirements
    columns = []
    for i in range(len(df.columns)):
        if i != 0:
            #find location of "(" and "in", then use that to trim column strings
            index_to_stop = df.columns[i].find(' (')+1 or df.columns[i].find(' in ')+1
            columns.append(df.columns[i][0:index_to_stop-1])
        else:
            columns.append(df.columns[i])

    df.columns = columns
    
    #Selecting columns specified in the excercise
    df = df[df.columns.tolist()[0:6]+df.columns.tolist()[7:9]]
    
    #Adding the year column
    df.insert(1, "Year", 2018)
    
    #remove non numeric characters
    for col in df.columns[2:]:
        if df[col].dtype == "O":
            df[col] = df[col].str.replace(r'\D+', '')
  
    ##Sort by Road deaths per Million Inhabitants column
    df = df.sort_values("Road deaths per Million Inhabitants").reset_index(drop=True)
    
    df.to_csv("data.csv",index=False)
    
    return df

url = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'
get_csv(url).head(20)