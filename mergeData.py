import pandas as pd

# Read the data
data2005 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2005.csv')
data2006 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2006.csv')
data2007 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2007.csv')
data2008 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2008.csv')
data2009 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2009.csv')
data2010 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2010.csv')
data2011 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2011.csv')
data2012 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2012.csv')
data2013 = pd.read_csv('LEHD_data/oh_rac_S000_JT00_2013.csv')

## Add year column to each data set
data2005['year'] = 2005
data2006['year'] = 2006
data2007['year'] = 2007
data2008['year'] = 2008
data2009['year'] = 2009
data2010['year'] = 2010
data2011['year'] = 2011
data2012['year'] = 2012
data2013['year'] = 2013


# Merge the data to create one sheet of 2005 - 2013 data 
data = pd.concat([data2005, data2006, data2007, data2008, data2009, data2010, data2011, data2012, data2013])

# Save the data to a new csv file fully merged
data.to_csv('LEHD_data/oh_rac_S000_JT00_2005_2013.csv', index=False)