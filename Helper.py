from nsetools       import Nse
from datetime       import datetime
from tkinter        import * 
from tkinter        import messagebox

import json
# path for text file containing details of id and pass 
user_file = #Add path here 
# sample path for opening a user specific data file
sample_id_path = #Add path here
# API AND HELPER FUNCTIONS #######################################

nse=Nse()
ALL_codes=nse.get_stock_codes()
d={}
f=open(user_file)
data = f.read()
d= json.loads(data)


def nse_get(code):
     s = nse.get_quote(code)
     if(s==None):
         raise Exception()
     buy1 = s['sellPrice1']
     name1 = s['companyName']
     per=s['pChange']
     return str(buy1),name1,per
# End of nse_get

def checktime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").split(':')
    if(int(current_time[0])>=10):
        if(int(current_time[0])<=14):
            return True
        elif(int(current_time[0])==15 and int(current_time[1])<=30):
            return True
        else:
            return False
    elif(int(current_time[0])==9 and int(current_time[1])>=30):
        return True
    else:
        return False
# End of checktime
                
def index():
   i = dict(nse.get_index_quote("nifty 50"))
   index_lp=i['lastPrice']
   return index_lp
# End of index

def user_details(id):
   id_file = sample_id_path+id+'.txt'
   with open(id_file) as f:
      data = f.read()
      di = json.loads(data)
      k = list(di.keys())
      return k[0], di[k[0]], di
# End of user_details

def buy(C,quantity,name,fund,dict):
     code=C.upper()

     q=int(quantity)
     s= nse.get_quote(code)
     if(s==None):
        messagebox.showerror("Error","Invalid Code")
        return
     buy1 = s['sellPrice1']
     s1=str(buy1)
  
     
     total_price = buy1*q
     if total_price > fund :
         return "Insufficient fund"
     else:
         if code in dict.keys():
             dict[code]+=q  
             fund-=total_price
             dict[name] = fund
             return "Sucessfully added in your portfolio"
         else:
             fund -= total_price
             dict[name] = fund
             dict[code] = q  
             return "Succesfully added"
# End of buy

def sell(C,quantity,name,fund,dict):
    code=C.upper()
    q = int(quantity)
    s= nse.get_quote(code)
    if(s==None):
        messagebox.showerror("Error","Invalid Code")
        return
    sell1 = s['sellPrice1']
    s1 = str(sell1)

    if code in dict.keys():
        if q > int(dict[code]):
            return "Not enough quantity"
        else:
            fund += float(q)*float(sell1)
            dict[name] = fund
            dict[code] = int(dict[code])-q
            if(dict[code] == 0):
                del dict[code]    
            return "Sold Successfully"
    else:
        return f"You have not {code} stock"
# End of sell

def search_m(name):
    try:
        ans1=[]
        ans2=[]
        for i in ALL_codes:
            if name.lower() in ALL_codes[i].lower():
                ans1.append(ALL_codes[i]+' ( '+i+' ) ')
                temp=nse.get_quote(i)
                if(temp==None):
                    messagebox.showerror("Error","Invalid Code")
                    return
                ans2.append(str(temp['sellPrice1']))
            
        return ans1,ans2 
    except:
        raise Exception()    
# End of search_m
