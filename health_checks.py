import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email

"""
Check some problems, such as:
1. Report an error if CPU usage is over 80%
2. Report an error if available disk space is lower than 20%
3. Report an error if available memory is less than 500MB
4. Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

def check_cpu_usage():
    """
    Check if CPU usage is over 80%
    """
    usage = psutil.cpu_percent(1)
    return usage < 80
 
def check_disk_usage(disk):
    """
    Check if available disk space is lower than 20%
    """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
 
def check_available_memory():
    """
    Check if available memory is less than 500MB
    """
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500
 
def check_localhost():
    """
    Check if the hostname "localhost" cannot be resolved to "127.0.0.1"
    """
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

to_be_checked = {
    check_cpu_usage(): "CPU usage is over 80%",
    check_disk_usage("/"): "Available disk space is less than 20%",
    check_available_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}

error = False
for action, message in to_be_checked.items():
    if not action: 
        error_message = message
        error = True

#Send the email
if error:
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
        print('Email has been sent')
    except NameError:
        pass