import pandas as pd


def avg_data(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv('data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='InVld' and i!='---':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average


if __name__=='__main__':
    lst_year=[]
    for year in range(2013,2019):     
        lst_year.append(avg_data(year))
