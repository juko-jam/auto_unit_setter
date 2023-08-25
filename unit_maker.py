import pandas
import datetime

weekDays = {'sat':0, 'sun':1, 'mon':2, 'tue':3, 'wen':4, 'thu':5, 'fri':6}
RweekDays = {num:name for name, num in weekDays.items()}

# hourTable = {8:"08:00", 9:"09:00", 10:"10:00", 11:"11:00", 12:"12:00", 13:"13:00", 14:"14:00", 15:"15:00", 16:"16:00", 17:"17:00"}
hourTable = [f'{i//2 + 8:0>2}:00 - {i//2 + 8:0>2}:30' if i%2 == 0 else f'{i//2 + 8:0>2}:30 - {(i+1)//2 + 8:0>2}:00' for i in range(18)]
dfIndex = ['master' if i%2 == 1 else list(weekDays.keys())[i//2] for i in range(10)]
print(dfIndex)


plan_counter = [0]


def make(schedule, sub_list, sub_dict, was_successful, current_num, last_num):

    if(not was_successful):
        return
    
    if(current_num >= last_num):
        schedule.log()
        plan_counter[0] += 1
        return

    for lesson in sub_dict[sub_list[current_num]]:
        
        #print(lesson.name, lesson.id)
        
        if(schedule.is_new_lesson_valid(lesson)):     
            schedule.add_new_lesson(lesson)
            #print(f'added : {lesson.name}:{lesson.id}')     
            make(schedule,sub_list,sub_dict,True,current_num + 1, last_num)
            schedule.revert()
        else:
            #print(f'intruption : {lesson.name}:{lesson.id}')
            make(schedule,sub_list,sub_dict,False,current_num + 1, last_num)

    

class Sch:
    def __init__(self):
        self.__calender = []
        self.__last_modified_days = []

        for i in range(7):
            self.__calender.append([])

    def has_intruption(self, stated_lesson, new_lesson) -> bool:
        if((stated_lesson.start_time <= new_lesson.start_time and  new_lesson.start_time < stated_lesson.end_time) or\
           (stated_lesson.start_time < new_lesson.end_time and new_lesson.end_time <= stated_lesson.end_time) or\
           (new_lesson.start_time < stated_lesson.start_time and stated_lesson.end_time < new_lesson.end_time) or\
           (stated_lesson.start_time == new_lesson.start_time and stated_lesson.end_time == new_lesson.end_time)):
            return True
        else:
            return False
    
    def can_be_added_to_day(self, new_lesson, day) -> bool:
        for added_lesson in self.__calender[weekDays[day]]:
                if(self.has_intruption(added_lesson,new_lesson)):
                    return False
                
        return True

    def is_new_lesson_valid(self,new_lesson) -> bool:
        for day in new_lesson.days:
            if(not self.can_be_added_to_day(new_lesson, day)):
                return False
            

        # for day in new_lesson.days:
        #     self.__calender[weekDays[day]].append(new_lesson)

        return True
    
    def add_new_lesson(self,new_lesson) -> None:
        for day in new_lesson.days:
            self.__calender[weekDays[day]].append(new_lesson)

        self.__last_modified_days.append(new_lesson.days)
    
    def revert(self) -> bool:
        if(len(self.__last_modified_days)):
            bad_days = self.__last_modified_days.pop()
            for day in bad_days:
                popped = self.__calender[weekDays[day]].pop()
                
            #print(f'popped : {popped.name}:{popped.id}')
            
            return True
        
        return False
    
    def log(self) -> None:
        #print(f'plan number [{plan_counter[0]}] : ')
        print()

        header_df = pandas.DataFrame()
        print(header_df)
        header_df.to_csv('res.xlsx',mode='a')
        df = pandas.DataFrame(index=dfIndex, columns=hourTable)

        for index, row in enumerate(self.__calender):
            for item in row:
                start_point = (item.start_time.hour - 8) * 2 + (item.start_time.minute //30)
                end_point = (item.end_time.hour - 8) * 2 + (item.end_time.minute //30)
                df.iloc[index* 2, start_point:end_point] = item.name
                df.iloc[(index * 2) + 1, start_point:end_point] = item.master
            
        df.to_csv('res.csv',mode='a')
            





                



            

    

            


class Lesson:
    # format:
    # name,id, HH:MM, Day1/Day2 or Day
    # name ->str
    # id -> str
    # sTime -> str (HH:MM)
    # eTime -> str (HH:MM)
    # days -> tuple (day1)
    def __init__(self,id,name,sTime,eTime,days,master):
        self.name = name
        self.__id = id
        self.__sTime = sTime
        self.__eTime = eTime
        self.__days = days
        self.__master = master

    def __str__(self):
        return f'{self.id:0>2}_{self.name}'
    
    @property
    def days(self):
        return self.__days # tuple
    
    @property
    def start_time(self):
        return self.__sTime
    
    @property
    def end_time(self):
        return self.__eTime
    
    @property
    def id(self):
        return self.__id
    @property
    def master(self):
        return self.__master
        

lesson_dict = {}
sub_list = []
table = pandas.read_excel('units2.xlsx')

for sub in table.loc[:,'name'].unique():
    sub_list.append(sub)
    lesson_dict[sub] = []

# print(f'sub list is  : \n {sub_list}')
# print(table.iloc[1])

for row in range(len(table)):

    record = table.iloc[row]

    name = record['name']
    id = record['id']
    sTime = record['start_time']
    eTime = record['end_time']
    days_tuple = tuple(record['daysOfWeek'].split('/'))
    master = record['master']

    lesson_dict[name].append(Lesson(id,name,sTime,eTime,days_tuple,master))



make(Sch(),sub_list,lesson_dict,True,0,len(sub_list))


print(plan_counter[0])




# for sub in (table.loc[:,"name"]).unique():
#     sub_list.append(sub)
#     lesson_dict[sub] = [] # a list of lessons





    



