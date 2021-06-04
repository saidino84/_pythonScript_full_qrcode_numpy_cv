from requests import get

ip =get('https://api.ipfy.org').text
print('My public IP is :{}'.format(ip))