# pandas = panel data analysis... it used in data preparation 
# # pandas has 2 parts = data series (1D) and dataframe(2D)
# Data series ma only one col.. either number or alphabets/letters or both (as it accepts the array or np.array from numpy)... starts with the index number zero or default is zero
import pandas as pd
import numpy as np
data = [10, 20, 30, 40, "abc"] # if you just enter number dtype is int but if you input mix dataype you get dtype=object...
ds = pd.Series(data)
ds1 = pd.Series(np.array([50,60,70])) # you can give your custom indexes from "index attribute in list"..
ds2 = pd.Series(range(1,6))
print(ds)
print(ds1)
print(ds2)

# number of data series combine = dataframe...

data1 = {'name' : ['A','B','C'],
         'city': ['amd','surat','bar'],
         'div' : ['D1','D2','D3'],
         'marks': [400,500,600]
        }

ds3 = pd.DataFrame(data1, columns=["div","marks","city"]) #you can choose the specific columns as well, if you want all the cols, remove the column attributes
print(ds3) 
print("=============================")
df1 = pd.DataFrame() # this will not give error...=
print(df1) # Empty DataFrame = Columns: [] & Index: []
print("=============================")

# pandas always reads in .csv file...
car_data = pd.read_csv("car.csv")
#print(car_data)

ds3.to_csv("new_csvfile.csv") # this function converts the dataframe into csv file... into the current directory..
print("=============================")
car_df = pd.DataFrame(car_data)
car_df.set_index("Model", drop=True, inplace=True) # it will set the default index to your custom index, drop means to remove that col (if not written it will show that col 2 times in dataframe or in .csv file ; inplace attribute means to make some permanent changes into the csv file or dataframe.)
print(car_df)
print("=============================")
print(type(car_df))
print(car_df.head()) # give the first five occurences 
print(car_df.head(2)) # custom first n occurences
print(car_df.tail(2))# gives custom n last occurence and if you remove int parameter,you get last 5 occurences
print(car_df.ndim)
print(car_df.shape)
print(car_df.dtypes)
print(car_df.sample(10)) # a random sample of items (rows or columns) from the DataFrame, returned as a new DataFrame object
print(car_df.columns) # Index(['Car', 'Volume', 'Weight', 'CO2', 'Unnamed: 5'], dtype='object')
print("=============================")

autompg_df = pd.read_csv("auto-mpg.csv")
autompg_df.info()
print(autompg_df)
print(autompg_df.describe()) # it gives basic statistical analysis of the dataframe. if the datatype of one col is object : then it cannot calculate the answers
print(autompg_df.describe(include="all")) # includes all the cols
print(autompg_df.describe(exclude=["float64"]))
print(autompg_df.describe(percentiles=[0.23,0.89,0.11])) # you can include your custom percentiles also
print("=============================")

cricket_data = {"name" : ["kohli", "rohit","gill","hardik"],
                "runs" : [1000,4500,6000,450],
                "average" : [23.4,40.5,90.99,34.89]
                }
cricket_df = pd.DataFrame(cricket_data)
print(cricket_df)
print(cricket_df.index) 
# to extract the whole col use below : 
print(cricket_df['runs'])
print(cricket_df[['name',"average"]])
# to extract rows and manipulate or make changes to particular data in a row, use "loc or iloc" function : (loc = location and iloc = index-wise location)
# to use these, imagine the exel file format and solve, or from 2D concepts.
# loc func = accepts parameter of index number and also name of the col to get the particular data in a row
# iloc = only accepts the index num as parameter. 
print("=============================")
print(cricket_df.loc[1])
print(cricket_df.iloc[1])
print(cricket_df.loc[0:3]) # gives rows from 0 to 3
print(cricket_df.iloc[0:3]) # gives rows from 0 to 2 (or n-1 rows)
print(cricket_df.loc[1,"average"])
print(cricket_df.iloc[1,2]) 

cricket_df.loc[1,"name"] = "xyz"
print("revised dataframe = ")
print(cricket_df)
# to add new rows = pick the last index; put into loc[index] and write data in list 
cricket_df.loc[4]= ["surya", 2000,60.3]
cricket_df.loc[6]= ["axar", 2000,60.3] # you can add data to random the col index num also.
#cricket_df.loc[7]= ["axar", 2000,60.3] # you can duplicate the data also 
print(cricket_df)
#to add a wole new col = use df["col_name"] = [data]
cricket_df["matches"] = [100,200,500,500,700,78]
# or we can add col like this way to using loc func = 
cricket_df.loc[:,"strike-rate"] = [98,87,90,67,86,34]
print(cricket_df)
cricket_df["performance"] = "good" # this LOC will put good to every row coz single data was inserted...
print(cricket_df)
# task : if the average is <50 , then change the performance data from good to average w/o if condition (HINT :  )

print("=============================")
sales_df = pd.read_csv("sales_data.csv")
print(sales_df)
print(sales_df.isna()) # you can also use .isnull() both are same... returns true in that specific cell where Nan exists and false if not .
print(sales_df.isna().sum()) #if you want total sum of nan data in a col
#print(sales_df.dropna()) # default parameter is : axis = 0; it will remove the whole row where there is NAN in a cell.
print(sales_df.dropna(axis=1)) # if any one data is Nan in col, it will remove the whole row.... if every col has even one Nan, then you get empty df
print(sales_df.dropna(thresh=3)) # thresh = n  will allow n number of non-Nan in a row else it will remove the whole row.
print(sales_df.dropna(how="all")) # it will remove all those rows which have every data nan
print(sales_df.dropna(how="any")) # it will remove all those rows which have any one data nan
print(sales_df.dropna(subset=["sales","expenses"])) # it will remove those rows where Nan exist in these specific colname like sales and expenses 
print("=============================")
# K3B : dropna() / dropna(how = any) / dropna (how = all) = ALL 3 are same , and give same answers
# fillna (number/new_data) = it will the particular data you passed as a parameter where the Nan exist in that cell... you can choose particular rows/col/whole df
print(sales_df.fillna(0)) # fills nan with 0 in whole df
print(sales_df["sales"].fillna(0))
print(sales_df["sales"].fillna(sales_df["sales"].mean())) # it means search Nan in the sales col in df and then replace or fill that Nan cell "with" the vale of mean of "sales" col..
print(sales_df.fillna(1.1111111111))