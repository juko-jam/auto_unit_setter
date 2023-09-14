# auto_unit_setter
a humble set of programs to make a plan for your semester
you can see final result in new_excel.xlsx
(and a simple version of that in _primary.xlsx)

to use first provide a excel file exactly like units.xlsx/units2.xlsx in this repo (notice that the headers should be identical (currently exam date is not necessary))

header discription :
id -> it's the id of the lesson (usually lessons are presented like ******_id) (it's not necessary to provide this if you like you can leave all id cells blank)

name -> it's the name of the lesson nothing special about it ( by the way you have controll over names it's not sth predefined i.g you can write ds instead of data structure)
just a hint the more concise is your choosen name the easier it is to read later

start_time -> you should enter what time a particular lesson starts ( format of time is like -> HH:MM;  some valid time -> 8:00, 09:10, 10:21 )

end_time -> no description _-_

daysOfWeek -> in this cell you will enter days onwhich this particular lesson is held ( you may only use sat/sun/mon/tue/wen/thu/fri)
if there is only one day then write that day like : sat or wen
if there are multiple days just seprate them with '/' like : sat/wen

master -> the name of the master for this particular lesson

exam date -> didn't provide a finall exam check so currently providing this cell is redundant

(see units.xlsx/units2.xlsx to understand how to make a valid spread sheet)


this is how you make your lessons' excel file. now how to run program ?

# let's discuss unit_maker.py 
at the top of this, there are two strings 

excel_to_read -> which is the excel file that you provided above ( or units.xlsx/units2.xlsx in this repo)
you should put the excel file and this py file in the same folder and set the value of this variable to the excel name ( Ofcourse, with its extension that is xlsx)

excel_to_write -> this will be the name of the file inwhich your plans will be saved ( make sure to provide its extension as "csv" i.e "AnyThing.csv")

that's it!
you can run this py file and your results will be saved in the save directory(folder) with the name you provided to excel_to_write variable


# its time to make it a little readable

after taking all those long steps you're here with a csv file that looks fussy and give you a headache to follow
in order to fix that first let's save the csv file as xlsx file (if you're using Microsoft Excel it will automatically suggest you to do that)

now open mergin_identical_cells.py in a editor

at the top of it, there are to strings again:

target_excel_file -> this is the file that you got from previous process (and saved as a xlsx file) so it should look like this "NameYouChoose.xlsx"

sheet_name -> this is the sheet in the target_excel_file that you provided above (if you followed the step as it was, your sheet name should be identcial to your excel file (for example if you name your excel file as sample.xlsx your sheet name is sample). if you are getting exception or errors check the sheet name manually)

that's it. run the py file and the excel file will become a lot more easier to read
(unfortunately this one will take while to process about 3 mins or more be patient with it)
(if you have any alternate way to make this work faster it's a pleasure to know that)

here we are at the last stage

if you want to make this even more eye comforting you can use coloringCells.py

# coloringCells.py

there are two important properties in this file 

excel_path -> you should provide the excel file you created from above i.e "Name.xlsx"

lesson_colors -> it's a dictionary containing lesson names as keys and their colors as a hexadecimal value (both string)
you should change it manually to match your needs

( if you see the examples and the current py files you will understand how to change it )




