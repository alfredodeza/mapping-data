This is a demo project to familiarize myself with Git and GitHub.

I converted the wine_ratings_small.csv to a pandas dataframe, then I
 extracted the name, region, variety, rating, and notes columns from the 
 resulting dataframe. After this I set the name column as the index, and 
 used Boolean masking to select only those wines whose rating was greater
 than or equal to 94.

From here, I converted this dataframe to a dict of dicts, where the format was
{name->{column_name-> value}}. From here I wrote this to a json file using
json.dump. I converted the wine_ratings_small.csv to a pandas dataframe, then I
extracted the name, region, variety, rating, and notes columns from
the resulting dataframe. After this I set the name column as the index,
and used Boolean masking to select only those wines whose rating was greater
than or equal to 94.

From here, I converted this dataframe to a dict of dicts, where the format was
{name->{column_name-> value}}. From here I wrote this to a json file using
json.dump.

