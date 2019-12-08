# DynamoDB and Python Project 
In this project we stick to the concepts of creating a table, loading items into a table, creating, updating and deleting items in a table, querying and scanning a table, creating a table with Local Secondary Index, and finally creating a Global Secondary Index.

As a prerequisite python3 and AWS CLI must be installed

Use ```aws configure``` in terminal to log into AWS provided that you have an account and IAM configured

## Create a table 
In this step you create a table named Movies.
Run the file named "MoviesCreateTable.py".

To run the program, type the following command:
```bash
pip3 install philter

python3 MoviesCreateTable.py
```
To create a table with Local Secondary Index run the file named "MoviesCreateTableLSI.py".

## Loading sample data
In this step you upload movie1.json file containing the data about movies.
Run the file named "MoviesLoadData.py".

To run the program, type the following command:
```bash
python3 MoviesLoadData.py
```

## Creating a new item
In this step you create a new item in the table
Run the file named "MoviesItemOps01.py".

To run the program, type the following command:
```bash
python3 MoviesItemOps01.py
```

## Reading an Item
In this step you read an item from the table
Run the file named "MoviesItemOps02.py".

To run the program, type the following command:
```bash
python3 MoviesItemOps02.py
```

## Updating an Item
In this step you update an item from the table
Run the file named "MoviesItemOps03.py".

To run the program, type the following command:
```bash
python3 MoviesItemOps03.py
```
To atomically increment the rating of a movie run the file named "MoviesItemOps04.py".
To conditionally update an item run the file named "MoviesItemOps05.py".

## Deleting an item
In this step you delete an item from the table
Run the file named "MoviesItemOps06.py".

To run the program, type the following command:
```bash
python3 MoviesItemOps06.py
```
To delete all the records in the table run the file named "MoviesScanandDelete.py".
## Querying
In this step you scan all the movies released in a year
Run the file named "MoviesQuery01.py".

To run the program, type the following command:
```bash
python3 MoviesQuery01.py
```
To query all the movies released in a year with certain titles run the file named "MoviesQuery02.py".

## Scanning
In this step you query all the movies released in between certain years
Run the file named "MoviesScan.py".

To run the program, type the following command:
```bash
python3 MoviesScan.py
```

## Creating a Global Secondary Index and querying an item using Global Secondary Index 
In this step you create a global secondary index for the attribute title
Run the file named "GSI.py".

To run the program, type the following command:
```bash
python3 GSI.py
```
To query an item using Global Secondary Index Run the file named "QueryingGSI.py".
