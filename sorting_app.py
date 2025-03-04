from tkinter import *
from tkinter import ttk,filedialog,messagebox
import os,shutil
class sorting_app:
    def __init__(self,root):
        self.root=root
        self.root.title("Sorting Application")
        self.root.geometry("1560x900+0+0")
        self.root.config(bg="White")
        self.logo_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\folder.png")
        title=Label(self.root,text="File Sorting Application",padx=10,image=self.logo_icon,compound=LEFT, font=("impact",35),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)


        
        #======================================================SECTION__1__===================================================  

        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=45,y=86)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",20),state='readonly',bg="lightyellow").place(x=250,y=90,h=40,width=550)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=850,y=86,width=120)
        hr=Label(self.root,bg="lightgrey").place(x=50,y=160,height=2,width=1400)

        
        #===================================================== SECTION__2__ ================================================== 
        #=============ALL EXTENSIONS===============


        self.image_extentions=["Image Extentions",".jpeg,",".png"]
        self.audio_extentions=["Audio Extentions",".amr",".mp3"]
        self.video_extentions=["Video Extentions",".mp4",".avi",".mpeg4",".3gp"]
        self.doc_extentions=["Document Extentions",'.doc','.xlsx',".ppt",".pptx",'.xls','.pdf',".zip",".rar",".csv",".docx",".txt",".rtf"]

        self.folders={
                'videos':self.video_extentions,
                'audios':self.audio_extentions,
                'images':self.image_extentions,
                'documents':self.doc_extentions,
            }

        lbl_support_ext=Label(self.root,text="Various Supported Extentions",font=("times new roman",25),bg="white").place(x=45,y=170)
        self.image_box=ttk.Combobox(self.root,values=self.image_extentions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.image_box.place(x=70,y=225,height=30)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extentions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.video_box.place(x=440,y=225,height=30)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extentions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.audio_box.place(x=800,y=225,height=30)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extentions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.doc_box.place(x=1170,y=225,height=30)
        self.doc_box.current(0)

        #================================================== SECTION__3__===========================================================================
        #=============ALL_IMAGE_ICONS=================

        self.image_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\im.png")
        self.audio_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\Audio.png")
        self.video_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\Video.png")
        self.document_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\document.png")
        self.other_icon=PhotoImage(file=r"F:\Third Year\Sem 2\FileSortingDesktoppp\images\question-mark.png")
                       
                        #================== OUTSIDE_FRAME =====================
        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=290,width=1390,height=300)
        self.lbl_total_files=Label(Frame1,text="Total Files",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)

                       #================== IMAGE_BOX=====================

        self.lbl_total_image=Label(Frame1,bd=2,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_image.place(x=30,y=60,width=210,height=220)

        self.lbl_total_audio=Label(Frame1,bd=2,relief=RAISED,image=self.audio_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_audio.place(x=300,y=60,width=210,height=220)

        self.lbl_total_video=Label(Frame1,bd=2,relief=RAISED,image=self.video_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#F08080",fg="white")
        self.lbl_total_video.place(x=570,y=60,width=210,height=220)

        self.lbl_total_document=Label(Frame1,bd=2,relief=RAISED,image=self.document_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#008080",fg="white")
        self.lbl_total_document.place(x=840,y=60,width=210,height=220)

        self.lbl_total_other=Label(Frame1,bd=2,relief=RAISED,image=self.other_icon,compound=TOP,font=("times new roman",20,"bold"),bg="gray",fg="white")
        self.lbl_total_other.place(x=1110,y=60,width=210,height=220)

        #===========================Section 3=========================================

        lbl_status=Label(self.root,text="STATUS:",font=("times new roman",22),bg="white").place(x=45,y=620)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",20,"bold"),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=620)

        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",20,"bold"),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=620)

        self.lbl_st_left=Label(self.root,text="",font=("times new roman",20,"bold"),bg="white",fg="orange")
        self.lbl_st_left.place(x=800,y=620)

        #=================BUTTONS=============#

        self.btn_clear=Button(self.root,text="CLEAR",bd=5,command=self.clear,font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=960,y=610,height=45,width=190)

        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="START",bd=5,font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1200,y=610,height=45,width=190)
       
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        cmbine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1
        # this is for calculating other files only
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                ext="."+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))


    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directry)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            # print(self.all_files)
        
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

            messagebox.showinfo("Success","All Files Has moved Successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_start.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please select folder")
    
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files")



    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder))


    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,self.other_name))   



root=Tk()
obj=sorting_app(root)
root.mainloop()         