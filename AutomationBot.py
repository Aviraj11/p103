import os 
import shutil
import pandas as pd
import plotly.express as px
import random
import time

def task():
    print("Hello there! I am an AutoMation Bot and I can complete any of these tasks for you! Please Select one of the tasks to proceed -")
    task_given = input("1 : Clean Desktop, 2 : Create a Draft, 3 : Exchange Files, 4 : Backup Files, 5 : Delete Files, 6 : Create any graph on given data, 7 : Mystery Game? - ")
    
    if(task_given == "1"):
        path = input("Please enter the Path to your Desktop")
        list_of_files = os.listdir(path)
        for file in list_of_files:
            name,ext= os.path.splitext(file)
            ext= ext[1:]
            if ext== ' ':
                continue
            if(os.path.exists(path + '/' + ext)):
                    shutil.move(path+'/'+file, path+'/'+ext+'/'+file )
            else:
                    os.mkdir(path +'/'+ext)
                    shutil.move(path+'/'+file, path+'/'+ext+'/'+file )
        print("Desktop Cleaned Successfully!")
    elif(task_given == "2"):
        draft = input("Please Enter the Matter for your Draft - ")
        file = open("draft.txt", "w") 
        file.write(draft) 
        file.close()
        print("File Created Successfully!")
    elif(task_given == "3"):
        fileA  = input("Enter the first File. - ")
        fileB = input("Enter the second File. - ")
        with open(fileA, 'r') as a:
            data_a = a.read()
    
        with open(fileB, 'r') as a:
            data_b = a.read()

        with open(fileA, 'w') as a:
            a.write(data_b)
    
        with open(fileB, 'w') as b:
            b.write(data_a)
        print("Files Exchanged Successfully!")
    elif(task_given == "4"):
        source = input("Enter the Path for the files you want to Backup - ")
        destination = input("Enter the Path for the Destination where you want to Backup the files - ")
        shutil.copy(source ,destination)
        print("File BackedUp Successfully!")
    elif(task_given == "5"):
        path = input("Please Enter the Path to the File/Folder you want to Delete - ")
        seconds = time.time()
        def remove_folder(path):
            if not shutil.rmtree(path):
                print("Path Removed Succesfully")
            else: 
                print("Unable to Delete the Path")
        
        def remove_file(path):
            if not os.remove(path):
                print("Path Removed Succesfully")
            else: 
                print("Unable to Delete the Path")
                
        def get_file_or_folder_age(path):
            ctime = os.stat(path).st_ctime
            return ctime

        if (os.path.exists(path)):
                for root_folder, folders, files in os.walk(path):
                    if(seconds >= get_file_or_folder_age(root_folder)):
                        remove_folder(root_folder)
                    else:
                        for file in files:
                            files_path = os.path.join(root_folder,file)
                            if(seconds >= get_file_or_folder_age(files_path)):
                                remove_file(files_path)
                        
                        for folder in folders:
                            folder_path = os.path.join(root_folder,folder)
                            if(seconds >= get_file_or_folder_age(folder_path)):
                                remove_folder(folder_path)
        else:
            os.remove(path)
    elif(task_given == "6"):
        print("Please select which Graph you want to make")
        graph = input("1 : Bar Graph, 2 : Line Graph, 3 : Scatter Graph.")

        if (graph == "1"):
            bar = input("Please put the Path for the Data represented in the Graph - ")
            x = input("Enter which value you want the X-Axis to represent - ")
            y = input("Enter which value you want the Y-Axis to represent - ")
            title = input("Enter the tilte for your Graph - ")
            df = pd.read_csv(bar)
            fig_b = px.bar(df, x= x, y= y, title = title)
            fig_b.show()
        if (graph == "2"):
            line = input("Please put the Path for the Data represented in the Graph - ")
            x_l = input("Enter which value you want the X-Axis to represent - ")
            y_l = input("Enter which value you want the Y-Axis to represent - ")
            color_l = input("Enter which value you want Color to represent - ")
            title_l = input("Enter the tilte for your Graph - ")
            df = pd.read_csv(line)
            fig_l = px.line(df, x= x_l, y= y_l, color = color_l, title = title_l)
            fig_l.show()
        if (graph == "3"):
            scatter = input("Please put the Path for the Data represented in the Graph - ")
            x_s = input("Enter which value you want the X-Axis to represent - ")
            y_s = input("Enter which value you want the Y-Axis to represent - ")
            size_s = input("Enter which value you want Size to represent - ")
            color_s = input("Enter which value you want Color to represent - ")
            title_s = input("Enter the tilte for your Graph - ")
            df = pd.read_csv(scatter)
            fig_s = px.scatter(df, x= x_s, y= y_s, size = size_s, color = color_s,size_max = 50, title = title_s)
            fig_s.show()
    elif(task_given == "7"):
        print("Hah! So you have to challenged ME to a Mystery game?")
        print("Well Good luck to you because trust me, you are going to need it. HA HA HA!!")
        print("i GIVE YOU THE GUESSIG GAME! DONT RUN OUT OF CHANCES OR ELSE...")
        number = random.randrange(1,9)
        chances = 5

        while chances > 0:
            guess = int(input("Your Guess - "))
            
            if guess>number:
                print("You guessed too High!")
                chances = chances -1
                continue
            elif guess<number:
                print("You Guessed too Low!")
                chances = chances -1
                continue
            elif guess==number:
                print("You Gussed Right! You got away Once but trust me, I wont let that happen again...")
                break
            elif chances == 0:
                def remove_folder(path):
                    if not shutil.rmtree(path):
                        print("HAHAHA")
                    else: 
                        print("Oops")
                
                def remove_file(path):
                    if not os.remove(path):
                        print("HAHAHA")
                    else: 
                        print("Oops")

                print("You ran out of Guesses! Now let the Fun begin...HA HA HA!!")
                path = "/PATH_TO_DELETE"
                
                if(os.path.exists(path)):
                    for root_folder, folders, files in os.walk(path):
                            remove_folder(root_folder)
                    else:
                        for file in files:
                            files_path = os.path.join(root_folder,file)
                            remove_file(files_path)
                        
                        for folder in folders:
                            folder_path = os.path.join(root_folder,folder)
                            remove_folder(folder_path)
                break

task()