months_dict = {
    "January": 1,
    "February": 2 ,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

def main():
    #while True:
        date = input("please type date-")
        print(arranged_date(date))
       # break



def arranged_date(date:str)->str:
    if "/" in date:
        month,day,year = date.split("/")
        if int(day) <= 31 and 12 >= int(month) >= 1:
            return f"{year}--{month:0>2}--{day:0>2}"
        else:
             return("your date is incorrect") 
    else:
          month_and_day,year = date.split(", ")
          month,day = month_and_day.split(" ")
          month=months_dict[month]
          if int(day) <= 31 and 12 >= int(month) >=1:
               return f"{year}--{month:0>2}--{day:0>2}"
          else:
               return("your date is incorrect")
               

          
         



if __name__=="__main__":
      main()



    