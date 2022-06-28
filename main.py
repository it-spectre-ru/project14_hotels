import requests


def get_data(url):
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive'
  }

  r = requests.get(url=url, headers=headers)

  with open('index.html', 'w') as file:
    file.write(r.text)


def main():
  get_data('https://www.tury.ru/hotel/most_luxe.php')


if __name__ == '__main__':
  main()