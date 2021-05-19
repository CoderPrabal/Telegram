import requests
import json
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_data(pin, date):
    r = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pin + "&date=" + date,
        headers=headers)
    data = r.json()
    check = r.text
    if 'Invalid Pincode' in check:
        return "invalid pincode"
    else:
        centers = data["centers"]
        if (len(centers) > 0):
            data_all = []
            for centre in centers:
                sessions = centre["sessions"]
                for session in sessions:
                    data_all.append({"centre_name": centre["name"], "centre_address": centre["address"],
                                     "availability": session["available_capacity"], "date": session["date"]})
            return (data_all)
        else:
            return ("no centre")

while(1):
    print("Inside While")
    welcom = "https://api.telegram.org/bot1822612112:AAFZS8xK5J8vWT5miyhqA7Dol_QiEvWLOPQ/sendMessage?chat_id=-558142978&text=Hello i m a bot"
    requests.get(welcom, headers=headers)
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    r = requests.get(url, headers=headers)
    data = r.json()
    check = r.text
    print(check)
    bot_district = "https://api.telegram.org/bot1822612112:AAFZS8xK5J8vWT5miyhqA7Dol_QiEvWLOPQ/sendMessage?chat_id=-558142978&text="+check+""
    requests.get(bot_district, headers=headers)
    time.sleep(900)

