from swampy.Gui import *
import Image as PIL
import ImageTk



def ab_app():
            abapp=Gui()
            abapp.row([0,1])
            abapp.la(text='This is an app developed to analyse the results of \n BMS College of Engineering, Grading system ')

def ab_dev():
            abdev=Gui()
            abdev.la(text='An app by Sujay HG')


def gpa_calc(data):
	i=-1
	j=-3
	gp=0
	for k in range(6):
		gp+= int(data[i]) * int(data[j])
		i-=3
		j-=3
	
	gp2=gp/25.0	
	return gp2




def final_res(ipusn):
            view=Gui()
            view.title('view results')
            fin=open('RES.txt')

            usn_gpa={}
            name_usn={}
            gpa_usn={}
            linesplit=[]
            gpaacc=[]
            usnacc=[]
            usn_name={}
            for line in fin:
                        linesplit=line.split(' ')
                        gpa=gpa_calc(linesplit)
                        usn_gpa[linesplit[1]]=gpa
                        usnacc.append(linesplit[1])
                        dell=' '
                        usn_name[linesplit[1]]=dell.join(linesplit[2:-18])
                        if gpa in gpa_usn:
                                    gpa_usn[gpa].append(linesplit[1])
                        else:
                                    gpa_usn[gpa]=[linesplit[1]]

                        if gpa not in gpaacc:
                                    gpaacc.append(gpa)

            gpaacc.sort(reverse=True)

            if ipusn not in usnacc:
                        view.la(text='Invalid USN\n Make sure you have entered the USN correctly')

            gpa2=usn_gpa[ipusn]
            for i in range(len(gpaacc)):
                           if gpaacc[i]==gpa2:
                                       rank=i+1
            view.row()
            view.col()
            view.la(text='Hello %s' %usn_name[ipusn])
            view.la(text='Your SGPA is %s' %gpa2)
            view.la(text='Your SGPA position is %i: ' %rank)
            view.endcol()
            gpa_usn[gpa2].remove(ipusn)
            view.col(padx=50)
            view.la(text='Your SGPA is tied with %s students' %len(gpa_usn[gpa2]))
            view.col(pady=50)
            view.col(padx=5)
            for u in gpa_usn[gpa2]:
                        var='%s  (%s)' %(usn_name[u], u)
                        view.la(text=var)
                        view.col(pady=5)
                        
                        
                        




def res():
            u=entry.get()
            final_res(u.upper())



win = Gui()
win.title('GPA Analysis')
win.row()
logo1=PIL.open('logo.png')
logo=ImageTk.PhotoImage(logo1)
win.la(image=logo)
win.row([0,0], padx=50)
win.la(text='Analysing 4th sem, ECE results \n of the year 2014')
win.col()
win.bu(text='About the app', command=ab_app)
win.bu(text='About the Developer', command=ab_dev)
win.la(text='Kindly mail your feedback to \n hgsujay@gmail.com')
win.endcol()
win.col([0,3],pady=70,padx=50)
win.la(text='Enter your USN')
entry=win.en(text='1BM12EC129')
win.bu(text='View result analysis', command=res)
win.endcol()
win.row([0,4], padx=1)
win.col()
bms=PIL.open('bmslogo.png')
bms=ImageTk.PhotoImage(bms)
win.la(image=bms)


win.mainloop()

