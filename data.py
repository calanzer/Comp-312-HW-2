import csv


#This will open our csv files and re-write the relevent rows to a new csv file this contains our zip-code to restaurant risk data
with open("Food_Inspections.csv","rb") as source:
    rdr= csv.reader( source )
    with open("Final_Food_Inspections.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[5], r[9] ))


#This will open our csv files and re-write the relevent rows to a new csv file this one contains our neighborhood poverty
with open("Socioeconomics_2008_2012.csv","rb") as source:
    rdr= csv.reader( source )
    with open("final_socioeconomic.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[1], r[3] ))


#Since our csv file for food inspections is based on zip-codes we will change the zip-code values to neighborhood values.
new_rows = []
changes = {
    '60660' : 'Edgewater',
    '60601' : 'Loop',
    '60602' : 'Loop',
    '60603' : 'Loop',
    '60604' : 'Loop',
    '60605' : 'Near South Side',
    '60606' : 'Near West Side',
    '60607' : 'Near South Side',
    '60608' : 'Bridgeport',
    '60609' : 'Armour Square',
    '60610' : 'Near North Side',
    '60611' : 'Near North Side',
    '60612' : 'Near West Side',
    '60613' : 'Lakeview',
    '60614' : 'Lincoln Park',
    '60615' : 'Grand Boulevard',
    '60616' : 'Armour Square',
    '60617' : 'Avalon Park',
    '60618' : 'Avondale',
    '60619' : 'Avalon Park',
    '60620' : 'Auburn Gresham',
    '60621' : 'Englewood',
    '60622' : 'Humboldt Park',
    '60623' : 'North Lawndale',
    '60624' : 'East Garfield Park',
    '60625' : 'Albany Park',
    '60626' : 'Rogers Park',
    '60627' : 'Riverdale Chicago',
    '60628' : 'Pullman',
    '60629' : 'Chicago Lawn',
    '60630' : 'Albany Park',
    '60631' : 'Edison Park',
    '60632' : 'Archer Heights',
    '60633' : 'Hegewisch',
    '60634' : 'Belmont Cragin',
    '60635' : 'Austin',
    '60636' : 'Chicago Lawn',
    '60637' : 'Greater Grand Crossing',
    '60638' : 'Clearing',
    '60639' : 'Austin',
    '60640' : 'Edgewater',
    '60641' : 'Avondale',
    '60642' : 'Beverly',
    '60643' : 'Beverly',
    '60644' : 'Austin',
    '60645' : 'West Ridge',
    '60646' : 'Forest Glen',
    '60647' : 'Hermosa',
    '60649' : 'South Shore',
    '60651' : 'Austin',
    '60652' : 'Ashburn',
    '60653' : 'Douglas',
    '60655' : 'Beverly',
    '60656' : 'O Hare',
    '60657' : 'Lakeview',
    '60659' : 'North Park',
    '60661' : 'Loop',
    '60664' : 'Near West Side',
    '60666' : 'O Hare',
    '60680' : 'Near West Side',
    '60681' : 'Near West Side',
    }

with open('Final_Food_Inspections.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        new_row = row
        for key, value in changes.items():
            new_row = [ x.replace(key, value) for x in new_row ]
        new_rows.append(new_row)

with open('Food_Inspection_neighborhood.csv', 'wb') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)

with open('Food_Inspection_neighborhood.csv', 'rb') as f:
    reader = csv.reader(f)
    food_list = list(reader)

with open('final_socioeconomic.csv', 'rb') as f:
    reader = csv.reader(f)
    Poverty_list = list(reader)


#I was unable to figure out a way to compare the two lists to make a correlation
for row[0] in Poverty_list:
    if row[1] in food_list == row[0] in Poverty_list:
        print row[0] in Poverty_list
        print(row[1] in Poverty_list/row[0] in food_list)














