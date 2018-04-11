# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:23:58 2018

@author: karja
"""

from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fil
import tkinter.messagebox as mes
import webbrowser
import os
from pathlib import Path
from textwrap import fill

# List of choices
choices = ('A', 'B', 'C')

# Class that have no properties yet
class S_at:
    pass

# Class that generate Windows console and stories from Blessing_Story folder
class Bless(S_at):
    
    def __init__(self,root):
        super().__init__()
        self.ch_st = []
        self.asw = None
        self.root = root
        root.title("Blessing Project")
        root.geometry("610x720+257+33")
        root.resizable(False,  False)
        
        # Binding short-cut for keyboard
        self.root.bind('<Control-d>', self.dele)
        self.root.bind('<Control-c>', self.copy)
        self.root.bind('<Control-s>', self.save_as)
        self.root.bind('<Control-x>', self.ex)
        self.root.bind('<Control-D>', self.dele)
        self.root.bind('<Control-C>', self.copy)
        self.root.bind('<Control-S>', self.save_as)
        self.root.bind('<Control-X>', self.ex)
        
        # Menu setting
        self.menu_bar = Menu(root)  # menu begins
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
        self.root.config(menu=self.menu_bar)  # menu ends
        
        # Help click to website
        self.about_menu = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label = 'About', menu = self.about_menu)
        self.about_menu.add_command(label = 'Help',compound='left', 
                                    command=self.about)
        
        # File menu
        self.file_menu.add_command(label='Save as',  compound='left', 
                                   accelerator='Ctrl+S', command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', compound='left', 
                                   accelerator='Ctrl+X', command=self.ex)
        
        # Edit menu
        self.edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                                   compound='left', command=self.copy)
        self.edit_menu.add_command(label='Delete', accelerator='Ctrl+D',
                                   compound='left', command=self.dele)
        
        # Variables to connect within widget.
        self.st1 = StringVar()
        
        # Checking the existence of the directory
        self.h_path = str(Path.home())
        
        try:
            self.root.iconbitmap(self.h_path + "\\Documents\\Bless_Story\\BlessingPro.ico")
            
            os.chdir('%s/Documents/Bless_Story' %self.h_path)
        except:
            mes.showinfo("Blessing Project", 'Please create story first! '+
                         'Check the folder "Bless_Story" in default local "Documents" folder!' +
                  ' If it is not exist, you should find it in your OneDrive(cloud) "Documents"' +
                  ' Please copy the folder to local "Documents" folder!')
            
            self.ex()
        else:
            
            # Cheking library for stories
            num_f = len([name for name in os.listdir()])
            if num_f is 0:
                input('Please create story first!')
            else:
                for name in os.listdir():
                    if name[-3:] == 'txt':
                        self.ch_st.append(name)
                    
        # Create frame, combobox, textbox, scrollbar, and radiobuttons
        self.combo = ttk.Combobox(root, values = self.ch_st, width = 30)
        self.combo.pack(side = TOP, pady = 3)
        self.combo.bind("<<ComboboxSelected>>", self.start_story)
        self.frame = Frame(root)
        self.frame.pack(side = BOTTOM, fill = BOTH, expand = True)
        self.scr = Scrollbar(self.frame)
        self.scr.pack(side = RIGHT, fill = BOTH, pady = 2, padx = 1)
        self.stbox = Text(self.frame, relief = 'sunken')
        self.stbox.pack(side = LEFT, fill = BOTH, expand = True,
                        padx = 2, pady = 2)
        self.scr.config(command=self.stbox.yview)
        self.stbox.config(yscrollcommand=self.scr.set)
        self.rb1 = Radiobutton(root, text = 'A', variable=self.st1, 
                               value = 'A', compound='left', 
                               command = self.choice, tristatevalue = 0)
        self.rb1.pack(side='left', expand = True)
        self.rb2 = Radiobutton(root, text = 'B', variable=self.st1, 
                               value = 'B', compound=LEFT, 
                               command = self.choice, tristatevalue = 0)
        self.rb2.pack(side='left', expand = True)
        self.rb3 = Radiobutton(root, text = 'C', variable=self.st1, 
                               value = 'C', compound=LEFT, 
                               command = self.choice, tristatevalue = 0)
        self.rb3.pack(side='left', expand = True)
        self.rb1.config(state = 'disable')
        self.rb2.config(state = 'disable')
        self.rb3.config(state = 'disable')
        
    # Choices function for choosing A/B/C    
    def choice(self, event = None):
        c = enumerate(choices)
        c = {a:b for b,a in c} 
        if str(self.st1.get()) == 'A':
            self.asw = c['A']
            self.g_ans()
        elif str(self.st1.get()) == 'B':
            self.asw = c['B']
            self.g_ans()
        elif str(self.st1.get()) == 'C':
            self.asw = c['C']
            self.g_ans()
                    
    # Answering function        
    def get_ans(self, ans=None, part=None):
        self.ans = ans
        self.part = part
        
        if self.part == 1:
            if self.ans == 0:
                self.stbox.insert(END, '\n' + 'Choose: ' + 'A')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansA)))
            elif self.ans == 1:
                self.stbox.insert(END, '\n' + 'Choose: ' + 'B')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansB)))
            elif self.ans == 2:
                self.stbox.insert(END, '\n' + 'Choose: ' + 'C')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansC)) + '\nThe End')
                
        elif self.part == 2:
            if self.ans == 0:
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'A')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansA)))
            elif self.ans == 1:
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'B')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansB)))
            elif self.ans == 2:
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'C')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansC)) + '\nThe End')
                
    # Filling stories parts into 9 set of class properties    
    def story(self):
        
        # Start with chosen story.
        self.docr = []
        file_op = open(self.combo.get(), 'r')
        file_op.seek(0)
        self.docr = file_op.readlines()
        ch1 = self.docr[1]
        ch2 = self.docr[2]
        
        # Fixing the choices list 
        self.fix_1=[]
        self.fix_2=[]
        post_1 = ''
        for appen in ch1:
            if appen != '[' != ']':
                post_1 += appen
                if appen == ',':
                    self.fix_1.append(post_1)
                    post_1 = ''
        self.fix_1 = [self.fix_1[i].replace(',','') 
                 for i in range(len(self.fix_1))] 
        
        post_2 = ''
        for appen in ch2:
            if appen != '[' != ']':
                post_2 += appen
                if appen == ',':
                    self.fix_2.append(post_2)
                    post_2 = ''
        self.fix_2 = [self.fix_2[i].replace(',','') 
                 for i in range(len(self.fix_2))] 
        file_op.close()

        # Setting up story to be run later on 
        S_at.pre = self.docr[0]    
        
        S_at.q1 = self.fix_1
        
        S_at.q2 = self.fix_2
        
        S_at.q1_ansA = self.docr[3]
        
        S_at.q1_ansB = self.docr[4]
        
        S_at.q1_ansC = self.docr[5]
        
        S_at.q2_ansA = self.docr[6]
        
        S_at.q2_ansB = self.docr[7]
        
        S_at.q2_ansC = self.docr[8]
        
    # Starting first part of a story
    def s_story1(self):
        
        # First part of the story
        self.stbox.insert("1.0 + 10 chars", str(fill(self.pre) + '\n'+'\n'))
        for i in self.q1:
            self.stbox.insert(END, i+'\n')
    
    # Get answer for first part of a story and second part of a story        
    def g_ans(self):
        if self.asw != None:
            if  str(self.q2[1]) in str(self.stbox.get("1.0",END)):
                self.get_ans(self.asw,2)
                self.s_story3()
                self.rb1.config(state = 'disable')
                self.rb2.config(state = 'disable')
                self.rb3.config(state = 'disable')
                self.stbox.config(state = 'disable')
            else:
                self.get_ans(self.asw,1)
                if str(self.st1.get())!='C':
                    self.s_story2()
                else:
                    self.rb1.config(state = 'disable')
                    self.rb2.config(state = 'disable')
                    self.rb3.config(state = 'disable')
                    self.stbox.config(state = 'disable')

    # 2nd part of a story
    def s_story2(self):
        print()
        self.stbox.insert(END, '\n')
        for i in self.q2:
            self.stbox.insert(END, '\n' + i )
            self.st1.set(1)
     
    # 3rd of a story           
    def s_story3(self):
        if self.asw == 0:
            w = self.docr[9] 
            print()
            self.stbox.insert(END, '\n')
            self.stbox.insert(END, '\n' + str(fill(w.upper(),73)) )
        elif self.asw == 1:
            w = self.docr[10]
            print()
            self.stbox.insert(END, '\n')
            self.stbox.insert(END, '\n' + str(fill(w.upper(),73)) )
    
    # Clear function for starting new story afresh    
    def clear(self):
        self.docr = []
        self.fix_1=[]
        self.fix_2=[]
        self.stbox.config(state = "normal")
        self.stbox.delete('1.0','end')
        self.rb1.config(state = 'normal')
        self.rb2.config(state = 'normal')
        self.rb3.config(state = 'normal')
        self.st1.set(1)

    # Start the story
    def start_story(self,event = None):
        self.clear()
        self.story()
        if len(self.docr) > 0:
            print()
            self.s_story1()
    
    # Link to lWW Github page
    def about(self):
        webbrowser.open_new(r"https://github.com/kakkarja/BP")
    
    # Select all text content
    def select_all(self):
        self.stbox.tag_add('sel', '1.0', 'end')
        return "break"
            
    # Generate Copy Function
    def copy(self, event = None):
        self.root.clipboard_clear()
        self.select_all()
        self.stbox.event_generate("<<Copy>>")
        return "break"
    
    # Generate Delete Function
    def dele(self, event = None):
        self.stbox.config(state = "normal")
        self.stbox.delete('1.0','end')
    
    # Generate Exit Function
    def ex(self, event = None):
        self.root.destroy()
    
    # Writing to a .txt file (misc) 
    def write_to_file(self,file_name):
        sen = str(self.combo.selection_get())
        try:
            content = sen + '\n'+'\n' + self.stbox.get('1.0', 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except:
            pass
    
    # Generate Save as function dialog
    def save_as(self, event = None):
        input_file_name = fil.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            self.write_to_file(file_name)
        return "break"
                
                

begin = Tk()
my_gui = Bless(begin)
begin.mainloop()