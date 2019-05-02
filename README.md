# Crime_Final_Project
This is an ML algorithm for predicting crime in Chicago in 2002. This code has been shortened to the first 100,000 entries in order to run on my computer
###STEPS TO RUN PROJECT
1. Download "Crimes_-_2001_to_present.csv" from the Chicago Crime Data Hub
2. Run pull_crime_data.py
3. Run data_improvement.py
  This does data cleaning, feature creation, and label encoding
4. Run randforestcrime.py
  This fits a random forest that has already been tuned by Grid Search to the data in question. 
  
  ###You Need pandas, scikit-learn, matplotlib, and csv to run this code
