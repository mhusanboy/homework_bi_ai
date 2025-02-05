import requests
import os 
from pathlib import Path 
import pdf2image
import time
import csv
import datetime



current_dir = Path(__file__).resolve().parent

#constants
folder = '/Users/mrhusanboy/Documents/empty/'
csvfile = current_dir / "statuses.csv"
token = os.environ.get('BOT_TOKEN')
admin_id = int(os.environ.get('ADMIN_ID'))
channel_id = os.environ.get('CHANNEL_ID')


url = f"https://api.telegram.org/bot{token}"



def getFirstPage(file):
    images = pdf2image.convert_from_path(file, first_page = 1, last_page = 1)
    image_path = file[:-4] + ".jpg"
    images[0].save(image_path, 'JPEG')
    return image_path




def sendMessage(chat_id, txt, *, reply_id = None):
    return requests.post(url + '/sendMessage', params={'chat_id' : chat_id, 'text' : txt, 'reply_to_message_id' : reply_id}).json()



def sendPhoto(chat_id, file, *, message = None, reply_id = None):
    with open(file, 'rb') as f:
        return requests.post(url + '/sendPhoto', 
                            data = {'chat_id' : chat_id, 'caption' : message, 'reply_to_message_id' : reply_id},
                            files = {'photo' : f}).json()


def sendDocument(chat_id, file, *, reply_id = None, message = None):
    with open(file, 'rb') as f:
        try:
            res = requests.post(url + '/sendDocument', 
                                    data = {'chat_id' : chat_id, 'caption' : message, 'reply_to_message_id' : reply_id}, 
                                    files = {'document' : f}).json()
            return res
        except:
            return None


def getDate(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def sendPdfsWithReply(folder):

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.pdf')]

    if not files:
        sendMessage(admin_id, "No pdfs found.")
        return

    fieldnames=["Pdf Title", "Size", "Status", "Date Sent"]
    with open(csvfile, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(fieldnames)
    
    
    sendMessage(admin_id, "Sending has started.")

    for f in files:
        with open(csvfile, 'a', newline='') as cf:
            writer = csv.writer(cf, delimiter=';')
            file_size = os.path.getsize(folder + f) / 1024

            status = 'Successful'
            date_sent = None

            image_path = getFirstPage(folder + f)
            img = sendPhoto(channel_id, image_path)
            os.remove(image_path)
            

            if img.get('ok'):
                res = sendDocument(channel_id, folder + f, reply_id=img['result']['message_id'])
                if not res:
                    status = 'Unsuccessful'
                else:
                    date_sent = getDate(res['result']['date'])

            writer.writerow([f, f"{file_size:.1f} KiB", status, date_sent])
    
    sendDocument(admin_id, csvfile, message='Log file for the current operations')
    os.remove(csvfile)
    
    


 



def run():
    
    req = requests.get(url + '/getUpdates').json()
    offset = 0
    if(req.get('result')):
        offset = req['result'][-1]['update_id'] + 1
        req = requests.get(url + '/getUpdates', params = {'offset' : offset}).json()

    while True:
        time.sleep(1)
        res = requests.get(url + '/getUpdates', params = {'offset' : offset}).json()
        if res.get('result'):
            responses = res.get('result')
            for response in responses:
                if response.get('message'):
                    m = response['message']

                    if m['from']['id'] == admin_id and m['text'] == '/start':
                        sendPdfsWithReply(folder)
                offset = response['update_id'] + 1

run()