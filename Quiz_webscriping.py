import requests
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
try:
    with open('Python Quiz Input - Sheet1.csv', 'r+') as input_file:
      csv_data = input_file.read().split('\n')
      input_file.seek(0)
      input_file.truncate()
      input_file.write(csv_data[0]+',Result\n')
      for i in csv_data[1:]:
        row = i.split(',')
        data = {'companyName' : row[0],
        'address1' : row[1],
        'address2' :"",
        'urbanCode' :"",
        'city' : row[2],
        'state' : row[3],
        'zip' : row[4].replace('\n','')}
        res = requests.post('https://tools.usps.com/tools/app/ziplookup/zipByAddress',headers = headers,data=data)
        if 'SUCCESS' in res.text:
          input_file.write(i+', Valid\n')
        else:
          input_file.write(i+', Invalid\n')
    print('File Has been Modified')
except Exception as e:
    print('Error : {}'.format(e))