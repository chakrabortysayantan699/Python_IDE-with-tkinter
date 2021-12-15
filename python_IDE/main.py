from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import os,path
import subprocess as sub
file_path=''

def set_file_path(path1):
	global file_path
	file_path=path1

def run():
	if file_path=='':
		save_promt=Toplevel()
		text=Label(save_promt,text='Please save your code')
		text.pack()
		# output=exec(code)
		# output.insert('1.0',output)
	else:
		command=f'python "{file_path}"'
		process=sub.Popen(command,stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
		output,error=process.communicate()

		output_place.insert('1.0',output)
		output_place.insert('1.0',error)
		# print(file_path)
		# print(output)
		# print(error)

def open_files():
	
	path=filedialog.askopenfilename(filetypes=[('Python Files','*.py')])
	with open(path, 'r' )as file:
		content=file.read()
		#editor=Text(content)
		editor.delete('1.0',END)
		editor.insert('1.0',content)
		set_file_path(path)

def open_folder():
	folder=filedialog.askdirectory(initialdir=os.path.normpath("C://"),title="Example")

def save():
	if file_path=='':
		path=filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')])
	else:
		path=file_path
	with open(path,'w')as file :
		code=editor.get('1.0',END)
		file.write(code)
		set_file_path(path)


def save_as():
	path=filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')])
	with open(path,'w')as file :
		code=editor.get('1.0',END)
		file.write(code)
		set_file_path(path)

compiler= Tk()
compiler.title("MY first IDE")

menu_bar=Menu(compiler)
compiler.config(menu=menu_bar)

file=Menu(menu_bar,tearoff=0)
file.add_command(label="New File")
file.add_command(label="Open File",command=open_files)
file.add_command(label="Open Folder",command=open_folder)
file.add_command(label="Save " ,command=save)
file.add_command(label="Save as" ,command=save_as)
menu_bar.add_cascade(label="File", menu=file)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label="Run", command=run)
run_bar.add_command(label="Build")
menu_bar.add_cascade(label="Execute",menu=run_bar)

quit=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="quit",menu=quit)
quit.add_command(label='exit',command=compiler.quit)

editor=Text()
editor.pack()

output_place=Text(height=10)
output_place.pack()

compiler.mainloop()
