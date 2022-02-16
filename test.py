#!/usr/bin/env python
import requests
import json
cookies = {
    'mac': '00%3A1A%3A79%3A2A%3A07%3AA3',
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
    'Referrer': 'http://vowiptv.com/stalker_portal/c/',
    'X-User-Agent': 'Model: MAG250; Link: WiFi',
    'Cache-Control': 'no-cache',
    'Host': 'vowiptv.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

params = (
    ('type', 'stb'),
    ('action', 'handshake'),
    ('token', ''),
    ('JsHttpRequest', '1-xml'),
)

response = requests.get('http://vowiptv.com/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)
a=f'Total users: {response.json().get("js")}'
b=a[24:56]
d=a[70:110]

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://vowiptv.com:-1/stalker_portal/server/load.php?type=stb&action=handshake&token=&JsHttpRequest=1-xml', headers=headers, cookies=cookies)
c='Bearer'+ " "+b

cookies = {
    'mac': '00%3A1A%3A79%3A2A%3A07%3AA3',
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
    'Referrer': 'http://vowiptv.com/stalker_portal/c/',
    'X-User-Agent': 'Model: MAG250; Link: WiFi',
    'Cache-Control': 'no-cache',
    'Authorization':c,
    'Host': 'vowiptv.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}
e='{"mac":"00:1A:79:2A:07:A3","sn":"","model":"MAG250","type":"STB","uid":"","random":"'+d+'"}'
params = (
    ('', ''),
    ('action', 'get_profile'),
    ('random', d),
    ('mac', '00:1A:79:2A:07:A3'),
    ('type', 'stb'),
    ('hd', '1'),
    ('sn', ''),
    ('stb_type', 'MAG250'),
    ('client_type', 'STB'),
    ('image_version', '218'),
    ('device_id', ''),
    ('hw_version', '1.7-BD-00'),
    ('hw_version_2', '1.7-BD-00'),
    ('auth_second_step', '1'),
    ('video_out', 'hdmi'),
    ('num_banks', '2'),
    ('metrics', e),
    ('ver', 'ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.6.1; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566'),
)

response = requests.get('http://vowiptv.com/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://vowiptv.com:-1/stalker_portal/server/load.php?=&action=get_profile&random=d526b87b8e8208459e647ce7e554a04f30ba2da9&mac=00%3A1A%3A79%3A2A%3A07%3AA3&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%2200%3A1A%3A79%3A2A%3A07%3AA3%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22d526b87b8e8208459e647ce7e554a04f30ba2da9%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566', headers=headers, cookies=cookies)





cookies = {
    'mac': '00%3A1A%3A79%3A2A%3A07%3AA3',
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'Accept': '/',
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
    'Referer': 'http://vowiptv.com/stalker_portal/c/',
    'Accept-Language': 'en-US,',
    'Accept-Charset': 'UTF-8,;q=0.8',
    'X-User-Agent': 'Model: MAG254; Link: WiFi',
    
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

params = (
    ('type', 'stb'),
    ('action', 'handshake'),
    ('token', ''),
    ('JsHttpRequest', '1-xml'),
)

response = requests.get('http://vowiptv.com/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)
f=response.text
g=f'Total users: {response.json().get("js")}'
h=a[24:56]
i=a[70:110]
j='Bearer '+h

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://vowiptv.com:-1/stalker_portal/server/load.php?type=stb&action=handshake&token=&JsHttpRequest=1-xml', headers=headers, cookies=cookies)


cookies = {
    'mac': '00%3A1A%3A79%3A2A%3A07%3AA3',
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'Accept': '/',
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
    'Referer': 'http://vowiptv.com/stalker_portal/c/',
    'Accept-Language': 'en-US,',
    'Accept-Charset': 'UTF-8,;q=0.8',
    'X-User-Agent': 'Model: MAG254; Link: WiFi',
    'Authorization': j,
    'Host': 'vowiptv.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

params = (
    ('type', 'account_info'),
    ('action', 'get_main_info'),
    ('JsHttpRequest', '1-xml'),
    ('mac', '00:1A:79:2A:07:A3'),
)

response = requests.get('http://vowiptv.com/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)



cookies = {
    'mac': '00%3A1A%3A79%3A2A%3A07%3AA3',
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'Accept': '/',
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
    'Referer': 'http://vowiptv.com/stalker_portal/c/',
    'Accept-Language': 'en-US,',
    'Accept-Charset': 'UTF-8,;q=0.8',
    'X-User-Agent': 'Model: MAG254; Link: WiFi',
    'Authorization': j,
    'Host': 'vowiptv.com:-1',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

params = (
    ('type', 'itv'),
    ('action', 'create_link'),
    ('forced_storage', 'undefined'),
    ('download', '0'),
    ('cmd', 'ffrt http://localhost/ch/7689'),
)

response = requests.get('http://vowiptv.com/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)

employee_dict = json.loads(response.text)
xy=(employee_dict['js'])
t=xy["cmd"]
url="demo.html#"+t
print(url)

