'''Python Program - GeoIP Lookup by DJ Harshit'''

# Importing the modules
from tkinter import *
from main import IP

# Functions
def retrieve():
	global out

	ip = IP()
	if var.get():
		ip.set_ip(e1.get())
	out = ip.start()
	l4.config(text='')

def set_data():
	global out
	retrieve()
	data = f'''
	Your IP : {out["ip"]}
	Continent Name : {out["continent_name"]}
	Country Name : {out["country_name"]}
	Region Name : {out["region_name"]}
	City Name : {out["city"]}
	Pin Code : {out["zip"]}
	Latitude : {out["latitude"]}
	Longitude : {out["longitude"]}

		Country Detail
	Country Name : {out["country_name"]}
	Country Capital : {out["location"]["capital"]}
	Country Call Code : {out["location"]["calling_code"]}'''
	l4.config(text=data)

def disable_ip():
	e1.config(state='disabled')

def enter_ip():
	e1.config(state='normal')


# Main program 
wind = Tk()
wind.geometry('500x500')
wind.resizable(0,0)
wind.title('GeoIP Location')

# Url variable
var = IntVar()
out = None

f1 = Frame(wind, width=500, height=100, pady=10)
f1.pack()
f2 = Frame(wind, width=500, height=100, pady=10)
f2.pack()
f3 = Frame(wind, width=500, height=300, padx=10)
f3.pack()

l1 = Label(f1, text='GeoIP Location', font=('SugarFont Bold', 30, 'bold'))
l1.grid(row=0, column=0, columnspan=3, padx=5)
l2 = Label(f1, text='By Harshit', font=('Arial Rounded MT Bold', 15))
l2.grid(row=0, column=4)

r1 = Radiobutton(f2, text='Your IP', font=('', 13), variable=var, value=0, command=disable_ip)
r1.grid(row=0, column=0)
r2 = Radiobutton(f2, text='Enter IP', font=('', 13), variable=var, value=1, command=enter_ip)
r2.grid(row=0, column=1)

l3 = Label(f2, text='Enter IP:', font=('', 13))
l3.grid(row=1, column=0, pady=5)
e1 = Entry(f2, width=50, state='disable')
e1.grid(row=1, column=1, pady=5)

b1 = Button(f2, text='Get', font=('', 13), command=set_data)
b1.grid(row=2, column=1)

l4 = Label(f3, font=('',13), justify='left')
l4.place(x=0, y=0)

wind.mainloop()