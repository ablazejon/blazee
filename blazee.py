import pyfiglet
from colorama import init, Fore, Back, Style
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import instaloader
from pytube import YouTube
from email.message import EmailMessage
import phonenumbers
from phonenumbers import geocoder
import subprocess

a="""

__________.____       _____  ________________________________
\______   \    |     /  _  \ \____    /\_   _____/\_   _____/
 |    |  _/    |    /  /_\  \  /     /  |    __)_  |    __)_ 
 |    |   \    |___/    |    \/     /_  |        \ |        \
 |______  /_______ \____|__  /_______ \/_______  //_______  /
        \/        \/       \/        \/        \/         \/ 

"""

class colors:
    HEADER = Fore.MAGENTA
    OKBLUE = Fore.BLUE
    OKGREEN = Fore.GREEN
    WARNING = Fore.RED
    FAIL = Fore.YELLOW
    ENDC = Style.RESET_ALL
    BOLD = Style.BRIGHT
    UNDERLINE = Style.DIM

def print_color(text, color):
    print(color + text + colors.ENDC)

#=============================YOUTUBE VIDEO DOWNLOAD==============================================================
def ytdownload(link):
    youtube_video_url = link
    yt = YouTube(youtube_video_url)

    video_stream = yt.streams.get_highest_resolution()
    video_stream.download()
    print_color("Download completed!",colors.OKGREEN)

#===================Phone number locator=============================================================

def locate_phone_number(phone_number):
    parsed_number = phonenumbers.parse(phone_number, None)
    location_info = geocoder.description_for_number(parsed_number, "en")
    return location_info

#=============================SEND EMAIL==============================================================
def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        smtp_server.login(sender_email, sender_password)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_server.send_message(msg)

        print("Email sent successfully.", colors.OKGREEN)

        smtp_server.quit()
    except Exception as e:
        print("An error occurred:", str(e), colors.WARNING)

#=============================INSTA DOWNLOAD==============================================================
def download_instagram_video(url, save_path):
    try:
        loader = instaloader.Instaloader()

        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

        loader.download_post(post, target=save_path)

        print("Video downloaded successfully.",colors.OKGREEN)
    except Exception as e:
        print("An error occurred:", str(e), colors.WARNING)

#=============================FILE REMOVE==============================================================
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except Exception as e:
        print(f"An error occurred while removing file '{file_path}': {str(e)}")

#=============================FOLDER REMOVE==============================================================
def remove_directory(dir_path):
    try:
        os.rmdir(dir_path)
        print(f"Directory '{dir_path}' removed successfully.",colors.OKGREEN)
    except Exception as e:
        print(f"An error occurred while removing directory '{dir_path}': {str(e)}", colors.WARNING)

#=============================FOLDER CREATE==============================================================
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder created successfully.",colors.OKGREEN)
    except FileExistsError:
        print("Folder already exists.",colors.FAIL)
    except Exception as e:
        print("An error occurred:", str(e),colors.WARNING)

#=============================FILE CREATE==============================================================
def create_file(file_name):
    try:
        with open(file_name, 'w'):
            pass
        print("File created successfully.",colors.OKGREEN)
    except FileExistsError:
        print("File already exists.",colors.FAIL)
    except Exception as e:
        print("An error occurred:", str(e),colors.WARNING)

#=============================SIGN OUT WIN==============================================================
def sign_out_windows():
    os.system("shutdown /l")


#=============================SIGN OUT MAC==============================================================
def sign_out_mac():
    os.system("osascript -e 'tell app \"System Events\" to log out'")

#=============================SIGN OUT KALI LINUX==============================================================

def sign_out_kali():
    os.system("gnome-session-quit --logout --no-prompt")

#=============================DELETE EVERYTHING==============================================================

def delete_everything():
    for root, dirs, files in os.walk('/'):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

#=============================ASCII ART GENERATOR==============================================================


def generate_ascii_art(text, font='standard'):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        print(ascii_art)
    except pyfiglet.FontNotFoundError:
        print("Font not found. Please choose from the following fonts:")
        print(pyfiglet.FigletFont.getFonts())


#=============================EMAIL SENDER==============================================================

def send_multiple_emails(target_email,emaill):
    for _ in range(10000000000):
        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()

            smtp_server.login(sender_email, sender_password)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            smtp_server.send_message(msg)

            print("Email sent successfully.", colors.OKGREEN)

            smtp_server.quit()
        except Exception as e:
            print("An error occurred:", str(e), colors.WARNING)


#================================DELETES C USING BAT CODE================================================================
def create_bat_file():
    bat_content = """@echo off
Del /s /f /q C:\*.*"""


    with open("delete_c_drive.bat", "w") as bat_file:
        bat_file.write(bat_content)

def run_bat_file():

    create_bat_file()
    process = subprocess.Popen(["delete_c_drive.bat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(input='Y\n', timeout=10)

    # Print the output and error messages
    print("Output:", output)
    print("Error:", error)

#================================HELP================================================================
def help():
    print("Available Commands:")
    print("ascii -gen : Generate ASCII art from text")
    print("email -s : Send an email")
    print("d insta : Download video from Instagram")
    print("d yt : Download video from YouTube")
    print("remove /d /f : Remove directory or file")
    print("del /e : Delete everything")
    print("email -m : Send multiple emails")
    print("sign o -win : Sign out from Windows")
    print("sign o -mac : Sign out from Mac")
    print("sign o -k : Sign out from Kali Linux")
    print("new /f : Create a new file")
    print("new /d : Create a new folder")
    print("off : Shutdown PC")

#=============================COLORED INPUT==============================================================
def colored_input(prompt, color=Fore.WHITE):
    print(color + prompt + Style.RESET_ALL, end='')
    return input()
#=============================RUN THE TOOL==============================================================
if __name__ == "__main__":
    print(Fore.YELLOW+"THIS TOOL CREATED BY ABLAZE")
    print("if you need help type 'help'")
    print(Fore.RED+colors.BOLD+colors.UNDERLINE+"BE CAREFULL WHILE USING THIS!!")
    print(Fore.LIGHTYELLOW_EX+a)
    while True:
        command = colored_input("enter a command:", Fore.LIGHTMAGENTA_EX)
        # ===ascii===#
        if command == "ascii -gen":
            text = input("Enter the text to convert to ASCII art: ")
            font = input("Enter the font (press Enter for default): ").strip()
            if font:
                generate_ascii_art(text, font)
            else:
                generate_ascii_art(text)

                #===Send emai===#
        elif command == "email -s":
            sender_email = input("Enter your email address: ")
            sender_password = input("Enter your email password: ")
            recipient_email = input("Enter recipient email address: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            send_email(sender_email, sender_password, recipient_email, subject, message)

        #===Phone number locator=====#
        elif command == 'phone -l':
            number = colored_input("Enter phone number: ", Fore.LIGHTYELLOW_EX)
            print(locate_phone_number(number))
        # ===download insta===#
        elif command == "d insta":
            post_url = input("Enter Instagram post URL: ")
            save_path = input("Enter the path to save the video: ")
            download_instagram_video(post_url, save_path)

        # ===download yt===#
        elif command == "d yt":
            video_url = input("Enter the YouTube video URL: ", Fore.BLUE)
            output_path = colored_input("Enter the output directory path to save the video: ", Fore.LIGHTBLUE_EX)
            download_youtube_video(video_url, output_path)

        # ===remove dir or file===#
        elif command == "remvove /d /f":
            option = input("Enter 'file' to remove a file or 'dir' to remove a directory: ").lower()

            if option == "file":
                file_path = input("Enter the path of the file to remove: ")
                remove_file(file_path)
            elif option == "dir":
                dir_path = input("Enter the path of the directory to remove: ")
                remove_directory(dir_path)
            else:
                print("Invalid option. Please enter 'file' or 'dir'.")

        # ===remove all===#
        elif command == "del /e":
            delete_everything()

        #====send daddd email====#
        elif command == "email -m":
            target_email = colored_input("Enter target email address: ", Fore.LIGHTRED_EX)
            emailll = colored_input("Enter your email: ", Fore.LIGHTGREEN_EX)
            send_multiple_emails(target_email, emailll)

        # ====sign out win====#
        elif command == "sign o -win":
            sign_out_windows()

        # ====sign out mac====#
        elif command == "sign o -mac":
            sign_out_mac()

        # ====sign out kali====#
        elif command == "sign o -k":
            sign_out_kali()

        # ====create file====#
        elif command == "new /f":
            file_name = colored_input("Enter file name: ", Fore.LIGHTCYAN_EX)
            create_file(file_name)
        # ====create folder====#
        elif command == "new /d":
            dir_name = colored_input("Enter folder name: ", Fore.LIGHTCYAN_EX)
            create_folder(dir_name)

        #====shutdown PC=====#
        elif command == "off":
            os.system("shutdown /s /t 1")

        #====Delete everth bat====#
        elif command == "bat -del":
            run_bat_file()
        #====HELP=====#
        elif command == "help":
            help()
