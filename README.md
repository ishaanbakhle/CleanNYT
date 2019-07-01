# CleanNYT
:newspaper: A python tool to clean and parse NexisUni's formatting of New York Times articles

## About

Created as part of a project that required identification of unique unilateral presidential actions mentioned in New York Times articles between 2001 and 2017.

To execute and write to a csv, input `df.to_csv('filename')`.

## Repository
`cleannyt.py` - A general script for processing NexisUni New York Times articles.

* The dataframe has `np.nan` values for data it fails to obtain.  These issues are challenging to resolve due to format inconsistencies in NexisUni's formatting of New York Times articles.  Gaps were filled with manual processing. All gaps were in date values, which were easy to manually resolved.

* The dataframe returned is in the following format:

| Index | Article Title | Date of Publishing | Full body text of the article |
|-------|---------------|--------------------|-------------------------------|


## Data Collection
The dataset that this tool was created for was extracted fully from NexisUni with the publication filter 'New York Times' being applied to all searches.  A table of search terms can be found below:

| **Year** | **Search Term**                                                                                                                 |
|----------|---------------------------------------------------------------------------------------------------------------------------------|
| 2001     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush OR Clinton)                 |
| 2002     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)                            |
| 2003     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)                            |
| 2004     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)                            |
| 2005     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)                            |
| 2006     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)            |
| 2007     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)          |
| 2008     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Bush)       |
| 2009     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama  |
| 2010     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)     |
| 2011     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)    |
| 2012     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)        |
| 2013     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)          |
| 2014     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)                  |
| 2015     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama)        |
| 2016     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Obama OR Trump)) |
| 2017     | ( "executive action" OR proclamation OR memorand* OR "executive agreement") AND president AND (Trump)      |




