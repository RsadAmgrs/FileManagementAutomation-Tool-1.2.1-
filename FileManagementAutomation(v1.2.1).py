import os
import pathlib
#By Rsad

#PATHS | all the stuff you need to rly change is js ts
#Change the last part of the paths to the name of the folder you want
src_mayeb = r'.'
DST_VIDS = r'.\VIDEOS'
DST_IMGS = r'.\IMAGES'
DST_AUDIO = r'.\AUDIO'
DST_EXECS = r'.\EXECUTABLES'
DST_DOCS = r'.\DOCUMENTS'
DST_PPTS = r'.\POWERPOINTS'
DST_SPRD = r'.\SPREADSHEETS'
DST_PRGRM = r'.\PROGRAMMING'
DST_MISC = r'.\MISC'

#CONSTANTS
FMA = (pathlib.Path(os.path.basename(__file__)).stem)
DIR = os.getcwd()
DIR_LIST= os.listdir('.') #current directory ts file is in

#FILE TYPES
VIDEOS = ['.mp4','.mov','.avi','.mkv','.wmv','.mpg']
IMAGES = ['.png','.jpg','.jpeg','.svg','.gif','.tif','.tiff','.webp','.bmp','.ico']
AUDIO = ['.mp3','.wav','.flac','.wma','.aac','.aiff','.ogg']
EXECUTABLES = ['.exe','.bat','.com','.cmd']
DOCS = ['.docx','.docm','.doc','.dotx','.dotm','.dot','.txt']
PPTS = ['.pptx','.ppt','.pptm','.potx','.pot','.potm','.pps','.ppsx','.ppam']
SPREADSHEETS = ['.xlsx','.xlsm','.xls','.xlsb','.xml','.xltx','.xltm','.xlt','.xls']
PROGRAMMING = ['.py','.json','.c','.php','.java','.cpp','.cs','.vb','.js','.css','.sql','.html',]
MISC = ['.pdf','.zip']

#FTL stands for File Types List
FTL = [VIDEOS,IMAGES,AUDIO,EXECUTABLES,DOCS,PPTS,SPREADSHEETS,PROGRAMMING,MISC] #add more for more file type range
dst_FTL = [DST_VIDS,DST_IMGS,DST_AUDIO,DST_EXECS,DST_DOCS,DST_PPTS,DST_SPRD,DST_PRGRM,DST_MISC]
str_dst = []



def dst_path_str():
    for dst in dst_FTL:
        sliced = dst[2:]
        str_dst.append(sliced)
    return str_dst

def main():
    display_main()
    file_check()

def display_main():
    print("You are currently using the File Management Automation Tool!")
    print()
    print("-----Here's some info-----")
    print(f"Current folder: {DIR}")
    print()
    print(f"Current number of files: {len(DIR_LIST)}")
    print()
    print("Current folders in directory:")
    folders_display()
    print()
    print()
    print()
    print("==========RUNNING MOVING FILES==========")

def folders_display():
    available_dir = []
    for folder in DIR_LIST:
        if pathlib.Path(folder).suffix == "":
            print(folder)
            available_dir.append(folder)
    check_av_dir(available_dir)

def check_av_dir(available_dir):
    here = []
    str_dst = dst_path_str()
    for dir in str_dst:
        if dir not in available_dir:
            here.append(dir)
        else:
            pass
    print()
    if len(here) > 0:
        
        print("The following folders are not here:")
        for missing in here:
            print(missing)
        print()
        print("These folders are required to store the files in.")
        print()
        print()
        print()
        input("Press 'Enter' to create folder/s")
        print("Making folders...")
        for missing in here:
            os.makedirs(missing)
        print("Folders made!")

    print("All required folders are present!")
    input("Press 'Enter' to continue")

def type_check(typ,cur_path,filename):
    if pathlib.Path(filename).stem == FMA:
        return None
    print(f"The file is \"{filename}\"")
    if typ == "":
        print("📁Extension is: none, most likely a folder")
        print("Not moving")
    else:
        print(f"Extension is: ", typ)
    for type in FTL:
        for ext in range(len(type)):
            cur_it = type[ext]
            if typ == cur_it:
                count=0
                for chunk in FTL:
                    if typ in chunk:
                        print(f"{filename} is {str_dst[count]}")
                        print(f"MOVING TO {dst_FTL[count]}")
                        dst_dst = os.path.join(dst_FTL[count], filename)
                        os.rename(cur_path,dst_dst)
                    else:
                        count+=1
            else:
                pass

def file_check():
    for filename in DIR_LIST:
        typ = pathlib.Path(filename).suffix
        cur_path = os.path.join(src_mayeb, filename)
        print()
        type_check(typ,cur_path,filename)
    print()
    input("FINISHED!")
    
#Rsad
main()
