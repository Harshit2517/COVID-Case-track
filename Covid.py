

from tkinter import *

root = Tk()
root.geometry('400x420+200+200')
root.title('Covid Tracker')

def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatch
    from covid import Covid
    
    covid= Covid()
    cases= []
    confirmed= []
    active= []
    recovered= []
    deaths= []
    
    root.update()
    countries= data.get()
    country_names= countries.strip()
    country_names= country_names.split(',')
        
    for x in country_names:
        cases.append(covid.get_status_by_country_name(x))
        root.update()
    for y in cases:
        confirmed.append(y['confirmed'])
        active.append(y['active'])
        recovered.append(y['recovered'])
        deaths.append(y['deaths'])
        
    confirmed_patch= mpatch.Patch(color='Red', label='Confirmed')
    active_patch= mpatch.Patch(color='Yellow', label= 'Active')
    recovered_patch= mpatch.Patch(color='Green', label= 'Recovered')
    deaths_patch= mpatch.Patch(color='Black', label= 'Deaths')
    
    plt.legend(handles=[confirmed_patch, active_patch, recovered_patch, deaths_patch])
        
    for x in range(len(country_names)):
        plt.bar(country_names[x], confirmed[x], color='red')
        if recovered[x]> active[x]:
            x_info=[active[x],recovered[x],deaths[x]]
            plt.bar(country_names[x], recovered[x], color='Green')
            plt.bar(country_names[x], active[x], color='yellow')
    
            #plt.pie(x_info, colors=['yellow', 'green', 'black'])
        else:
            x_info=[active[x],recovered[x],deaths[x]]
            plt.bar(country_names[x], active[x], color='Yellow')
            plt.bar(country_names[x], recovered[x], color='Green')
            plt.bar(country_names[x], deaths[x], color='Black')
            
    plt.title('Current Covid Stats')
    plt.xlabel('Country')
    plt.ylabel('Cases (in millions)')
    plt.show()

###################################################################################################################################################################

Label(root, text='COVID Details Finder',font=('Arial', 20), bg= 'blue', fg='White').grid(row=0, column=0)

lb_2= Label(root, text='Enter the name of country: ', font= ('Arial', 20), bg='blue', fg= 'White')
lb_2.grid(row=1, column=0, columnspan=2)

data= StringVar()
data.set('Seperate country names by , if entering 2  or more Countries.')

entry= Entry(root, textvariable= data, width=30, font=('Arial', 12))
entry.grid(row=1, column=2)

but_1= Button(root, text= 'Get Data', font=('Arial', 12), bg='skyblue', border=5, command= showdata)
but_1. grid(row=2, column=0)

#################################################################################################################################################################
        
root.mainloop()
    
