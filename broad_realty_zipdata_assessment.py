# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:45:05 2016

@author: Connor
"""
import os
import pdb
import pandas as pd
from file_walk_with_me import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects


plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 10})


# location of unscrubbed (for knoxville) realty data, hundreds of MB, so excluded
# from the repo, you can find th files from zillow on their data page
source_directory = 'C:\Users\lp0ougx3\Desktop\Development\generalized_realty\\raw_data'
output_directory = 'C:\Users\lp0ougx3\Desktop\Development\generalized_realty\\filtered_data'

# run filter walk when you need to generate new filtered files, otherwise it's
# just an overhead on the whole script running

# region filter is a list fo filter(s) (like zip codes) that will filter the data
# Currently running some northern virginia zip codes
region_filter = [22046, 22042, 22043, 22205, 22044, 22207, 22203, 22201, 22204,
                 22211, 22202, 22041, 22180]
str_filter = str(region_filter)

filter_walk(source_directory, output_directory, 'RegionName', region_filter)

file_names = file_walk(output_directory)


# dictionary format for graphing labels and such
# file_name_dict = {fileNames[0]:[xlabel, ylabel, title], }

file_name_dict = {file_names[0]:['Date', 'Number Available', 'Inventory Smooth, Seasonally adjusted'],
                  file_names[1]:['Date', 'Number Available', 'Median of weekly snapshot of for-sale homes'],
                  file_names[2]:['Date', 'Number Sold', 'Homes Sold in a Given Month'],
                  file_names[3]:['Date', 'Ratio', 'Ratio of Homes Sold as Foreclosures to All Homes'],
                  file_names[4]:['Date', '$', 'Seasonal Adjustment All Homes Median Price Cut'],
                  file_names[5]:['Date', '$', 'Seasonal Adjustment Condos Residence Median Price Cut'],
                  file_names[6]:['Date', '$', 'Seasonal Adjustment Single Family Residence Median Price Cut'],
                  file_names[7]:['Date', '$', 'All Homes Median Price Cut'],
                  file_names[8]:['Date', '$', 'Condos Median Price Cut'],
                  file_names[9]:['Date', '$', 'Single Family Residence Median Price Cut'],
                  file_names[10]:['Date', '$', 'Median Price for 1 Bedroom'],
                  file_names[11]:['Date', '$', 'Median Price for 2 Bedroom'],
                  file_names[12]:['Date', '$', 'Median Price for 3 Bedroom'],
                  file_names[13]:['Date', '$', 'Median Price for 4 Bedroom'],
                  file_names[14]:['Date', '$', 'Median Price for 5+ Bedrooms'],
                  file_names[15]:['Date', '$', 'Median Price for All Homes'],
                  file_names[16]:['Date', '$', 'Median Price for Condos/Co-ops'],
                  file_names[17]:['Date', '$', 'Median Price for Duplex/Triplex'],
                  file_names[18]:['Date', '$', 'Median Price for Single Family Residences'],
                  file_names[19]:['Date', '$/sqft', 'Median Price per sqft for 1 Bedroom'],
                  file_names[20]:['Date', '$/sqft', 'Median Price per sqft for 2 Bedroom'],
                  file_names[21]:['Date', '$/sqft', 'Median Price per sqft for 3 Bedroom'],
                  file_names[22]:['Date', '$/sqft', 'Median Price per sqft for 4 Bedroom'],
                  file_names[23]:['Date', '$/sqft', 'Median Price per sqft for 5+ Bedrooms'],
                  file_names[24]:['Date', '$/sqft', 'Median Price per sqft for All Homes'],
                  file_names[25]:['Date', '$/sqft', 'Median Price per sqft for Condos/Co-ops'],
                  file_names[26]:['Date', '$/sqft', 'Median Price per sqft for Duplex/Triplex'],
                  file_names[27]:['Date', '$/sqft', 'Median Price per sqft for Single Family Residences'],
                  file_names[28]:['Date', 'Percent (%)', 'Median of the monthly percentage price reduction for All Homes'],
                  file_names[29]:['Date', 'Percent (%)', 'Median of the monthly percentage price reduction for Condos/Co-ops'],
                  file_names[30]:['Date', 'Percent (%)', 'Median of the monthly percentage price reduction for Single Family Residences'],
                  file_names[31]:['Date', '$', 'Median Sold Price For All Homes'],
                  file_names[32]:['Date', '$/sqft', 'Median Sold Price per sqft For All Homes'],
                  file_names[33]:['Date', '$/sqft', 'Median Sold Price per sqft For Condos'],
                  file_names[34]:['Date', '$/sqft', 'Median Sold Price per sqft For Single Family Residences'],
                  file_names[35]:['Date', 'ZHVI/sqft', 'Median Value per sqft For All Homes'],
                  file_names[36]:['Date', 'Percent (%)', 'Percentage of homes with decreased value in the past year'],
                  file_names[37]:['Date', 'Percent (%)', 'Percentage of homes with increased value in the past year'],
                  file_names[38]:['Date', 'Percent (%)', 'Percentage of All Homes with a price cut during the month'],
                  file_names[39]:['Date', 'Percent (%)', 'Percentage of Condos with a price cut during the month'],
                  file_names[40]:['Date', 'Percent (%)', 'Percentage of Single Family Residence with a price cut during the month'],
                  file_names[41]:['Date', 'Percent (%)', 'Percentage of All Home Transactions that are Previously Foreclosed'],
                  file_names[42]:['Date', 'Ratio', 'Price to Rent Ratio for All Homes'],
                  file_names[43]:['Date', 'Count', 'Percentage of All Region Homes Sold in the Past Year'],
                  file_names[44]:['Date', 'Count', 'All Unsold REO Homes'],
                  file_names[45]:['Date', 'ZHVI', '1 Bedroom Zillow Home Value Index (ZHVI)'],
                  file_names[46]:['Date', 'ZHVI', '2 Bedroom Zillow Home Value Index (ZHVI)'],
                  file_names[47]:['Date', 'ZHVI', '3 Bedroom Zillow Home Value Index (ZHVI)'],
                  file_names[48]:['Date', 'ZHVI', '4 Bedroom Zillow Home Value Index (ZHVI)'],
                  file_names[49]:['Date', 'ZHVI', '5+ Bedroom ZHVI'],
                  file_names[50]:['Date', 'ZHVI', 'All Homes Zillow Home Value Index (ZHVI)'],
                  file_names[51]:['Date', 'ZHVI', 'Condos Zillow Home Value Index (ZHVI)'],
                  file_names[52]:['Date', 'ZHVI', 'Single Family Residences ZHVI'],
                  file_names[53]:['Date', 'ZRI', 'All Homes Zillow Rent Index (ZRI)'],
                  file_names[54]:['Date', 'ZRI', 'All Homes Plus Multifamily Zillow Rent Index (ZRI)'],
                  file_names[55]:['Date', 'ZRI', 'Zillow Rent Index (ZRI) per sqft for All Homes']}


graph_output_directory = 'C:\Users\lp0ougx3\Desktop\Development\generalized_realty\\'+str_filter+'_results\\'

if not os.path.exists(graph_output_directory):
    os.makedirs(graph_output_directory)    


# generate dataframes for all files from the filtered files, then some graphing    
for fname in file_names:
    plt.close()
    df = pd.read_csv(output_directory + '\\' + fname)
    col_count = len(df.columns)
    if df.columns[col_count-1] != '2015-12':
        print "Not time series data"
    else:
        y = range(0,36)
        x = []
        #print fname
        labels = df.columns[col_count-36:col_count]
        for i in range(col_count-36,col_count):
            #print i
            #pdb.set_trace()
            try:
                x.append(df.ix[0][i])
            except IndexError:
                x.append(0)
        
        #y = [y+0.5 for y in y]        
        
        plt.plot(y,x, linewidth = 4)
        plt.xlabel(file_name_dict[fname][0])
        plt.ylabel(file_name_dict[fname][1])
        plt.xticks(y, labels, rotation=45)
        if fname[0:3] == 'Zip':
            
            #plt.title(fname[4:-4]+' '+df.columns[col_count-37]+' to '+df.columns[col_count-1])
            plt.title(str_filter + ': '+file_name_dict[fname][2])
            plt.savefig(graph_output_directory+fname[4:-4]+'.png', dpi = 300)
        else:
            plt.title(str_filter + ': '+file_name_dict[fname][2])
            plt.savefig(graph_output_directory+fname[:-4]+'.png', dpi = 300)          



# not doing this, because I was just creating lsts of strings, I think I can do it
# all in the initial loop of df creation, consolidate it all, and I also don't have 
# to worry about data processes

## generate list of dataframe names
#df_names = []
#for fname in file_names:    
#    df_names.append(fname[:-4])
#    
#for df in df_names:
#    col_count = len(df.columns)
#    print col_count