# Road Safety In Europe database. 

Road safety in Europe encompasses transportation safety among road users in Europe, including automobile accidents, pedestrian or cycling accidents, motor-coach accidents, and other incidents occurring within the European Union or within the European region of the World Health Organization (49 countries). 

The Data from that database was scraped from [here]

[here]: http://www.imf.org/external/ns/cs.aspx?id=29



## Data

The source database is made of the 2018 values for each country consisting of the following columns:
Country,Year,Area,Population,GDP per capita,Population density,Vehicle ownership,Total Road Deaths,Road deaths per Million Inhabitants

I scraped this data and cleaned into a csv file:
* Dataset - `data.csv` - the dataset


## Run Script
pip3 install -r requirements.txt

python3 app.py

