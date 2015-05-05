##################################################################################################################
# 	                  Date:May 5  2015					                                                            		 #
# 	                  Author : Ermias Bayu,  Osmania University ,Hyderabad India    					              		 #
#       A python code to read list of countries from a csv 	 file and create directories for each countries      #
#	list of counties source :http://kejser.org/resources/free-data/free-data-countries-world/			            		 #
##################################################################################################################

import csv
import subprocess
def csv_dict_reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter='|')
	countrylist = []
	for line in reader:
		countrylist.append(line["CountryName"])	
	print("Started Creatting folders")
	#Loop through the array and create the folders
	for x in xrange(0,len(countrylist)):		
		subprocess.call("mkdir \\world\\\"" + countrylist[x] +"\"", shell=True)
	print("Finished Creatting folders")
	#Display the folders Created
	subprocess.call("dir \world", shell=True)
if __name__ == "__main__":
	with open("Country.csv") as f_obj:
		csv_dict_reader(f_obj)
