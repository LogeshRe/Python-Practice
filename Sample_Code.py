import tkinter as tk
from tkinter.filedialog import askdirectory
from os import listdir
import os, xlrd, xlwt, win32api
from xlutils.copy import copy
List_BoBc = []
Dict_BoBc = {}

def Readpath():
    foldername = askdirectory()
    return foldername

def xlfinder(original_folder):
    list_of_files = listdir(original_folder)
    list_of_xl_files = []
    child_list_of_xl_files = []
    for name in list_of_files:
        new_path = original_folder + '/' + name
        if(os.path.isdir(new_path)):
            temp_list = xlfinder(new_path)
            if(temp_list != []):
                child_list_of_xl_files.extend(temp_list)
        else:
            if(name[-4:]=='.xls'):
                list_of_xl_files.append(new_path)

    if(child_list_of_xl_files != []):
        list_of_xl_files.extend(child_list_of_xl_files)

    return list_of_xl_files



def xlpresent(filename):
    rb = xlrd.open_workbook(filename)
    sh = rb.sheet_by_index(0)
    BoBc = sh.cell_value(7,8)+'-'+ sh.cell_value(8,8)    
    #    createbook(filename,BoBc)
    if BoBc in Dict_BoBc:
        Dict_BoBc[BoBc].appenddata(filename)
    else:
        Dict_BoBc[BoBc] = xlwrite(filename)


class xlwrite:
    def __init__(self,filename):
        self.filename = filename
        read_workbook = xlrd.open_workbook(self.filename)
        read_sheet = read_workbook.sheet_by_index(0)
        self.rows_count = read_sheet.nrows
        self.cols_count = read_sheet.ncols
        self.write_workbook = copy(read_workbook)

    def appendata(self,filename):
        data_xl = xlrd.open_workbook(filename)
        data_sheet = data_xl.sheet_by_index(0)


def copywb(filename,sheet2):
    rb = xlrd.open_workbook(filename,formatting_info=True)
    rb1 = xlrd.open_workbook(sheet2)
    wb = copy(rb)
    #os.startfile(filename)
    #wb = win32com.client.GetObject(filename)
    ws = wb.get_sheet(0)
    rb_sheet = rb.sheet_by_index(0)
    rb1_sheet = rb.sheet_by_index(0)
    rb_sheet_rows = rb_sheet.nrows
    rb_sheet_cols = rb_sheet.ncols
    rb1_sheet_rows = rb1_sheet.nrows
    for i in range(14,rb1_sheet_rows):
        for j in range(3,rb_sheet_cols):
            ws.write(rb_sheet_rows,j,rb1_sheet.cell_value(i,j))
        rb_sheet_rows += 1
    wb.save(filename[:filename.rfind('/')+1] + 'Out_' + filename[filename.rfind('/')+1:filename.rfind('.')] + '.xls')

'''def newcheck(filename):
    import openpyxl
    mywb = openpyxl.load_workbook(filename)
    mywb.save(filename[:filename.rfind('/')+1] + 'Out_' + filename[filename.rfind('/')+1:filename.rfind('.')] + '.xls')'''
class sampleapp(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		lb = tk.Listbox(self)
		self.lists = []
		for values in listdir(openfile()):
			lb.insert("end",values)
		#lb.insert("end","one")
		#lb.insert("end","two")
		#lb.insert("end","three")
		lb.bind("<Double-Button-1>", self.OnDouble)
		#lb.bind("<Button-1>", self.OnDouble)
		lb.pack(side="top", fill="both", expand=True)
		button = tk.Button(lb, 
                   text="Process", 
                   fg="red",
                   command=self.testu(self))
		button.pack(side=tk.BOTTOM)
		button = tk.Button(lb, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
		button.pack(side=tk.BOTTOM)


	def OnDouble(self, event):
	    widget = event.widget
	    selection=widget.curselection()
	    value = widget.get(selection[0])
	    #print("selection:", selection, ": '%s'" % value)
	    testu(value)
	    print(self.lists)

	def testu(self, lists):
		print(self.lists)



def main():
	#original_folder = Readpath()
	#Files = xlfinder(original_folder)
	copywb('C:/Users/Logesh/Desktop/Retrofit Automation/New folder/1_C3D List of Values Loader.xls','C:/Users/Logesh/Desktop/Retrofit Automation/New folder/2_C3D List of Values Loader.xls')
	#newcheck('C:/Users/Logesh/Desktop/Retrofit Automation/New folder/1_C3D List of Values Loader.xls')


if __name__ == '__main__':
	main()