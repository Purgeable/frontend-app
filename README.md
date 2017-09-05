# mini-kep-app
Flask app with API to get macroeconomic time series

## v.0.1 - three bare CSVs with github webhook

App address <app>:

   - <kep.heroku address> or custom domain

Backends:

   - <app>/annual 
   - <app>/quarterly
   - <app>/monthly
   
   Backends deliver dfa.csv, dfq.csv, dfm.csv
   
Testing:
 
```python 
   
   # getter is https://github.com/epogrebnyak/mini-kep/blob/master/src/getter.py, can copy code to actual test
   
   from getter import read_csv, get_dataframe_from_repo  
   
   sources = dict(a='<app>/annual', 
                  q='<app>/quarterly',
				  m='<app>/monthly') 
				  
   for freq, url in sources.items():
	   df_repo = get_dataframe_from_repo(freq)
	   df_app = read_csv(url)
	   assert df_repo.equals(df_app)  
     
```
   
Github webhooks:

   On ```issue_comment``` or ```release```  three CSV files are updated in app
   

Extensions (not todo now):
  - custom domain/URL
  - frontpage with some welcome comments or intro at '/'

## Proposed enhancements

- requests log to catch popular series: <https://fred.stlouisfed.org/#popular-series>

- url for the list of variable names ```<app>/names```
  - needs a list of these names to be created in repo (not done yet)
  - also nice to organise it by section 
  - the sections can be used to list variables on frontpage

- put *here is the latest data* on frontpage
  - can prototype it at mini-kep README.md 
  - depends on <https://github.com/epogrebnyak/mini-kep/issues/78>
  
- interface to get specific variables, not just all dataframe 

```python
get_ts('m', 'CPI_rog') #  just one variable by varname
get_group('q', 'CPI')  #  variables starting with CPI*
get_df('a', ['CPI_rog', 'RETAIL_SALES_rog', 'SOC_WAGE_rog']) # several variables by names

# maybe this should be a call to like:
get(freq, vars)
# where *vars* may be a string or a list of varname(s) and/or varpattern(s)

#not todo - always on client side: trimming dates, variable transformations 
```
