import requests
import pprint
from bs4 import BeautifulSoup as bs


def get_file_extension_list():
    files_sign_list = list()
    for num_of_page in range(1, 19):
        page = requests.get(f'https://filesignatures.net/index.php?page=all&currentpage={num_of_page}&order=EXT&alpha=All')
        print(num_of_page)
        if page.status_code == 200:
            soup = bs(page.text, 'html.parser')
            table = soup.find('table', {'id': 'innerTable'})
            trs = table.find_all('tr')
            del trs[0]
            file_info = dict()
            for tr in trs:
                extension = tr.find('td', {'width':'147'}).text
                signature = tr.find('td',{'width':'236'}).text
                description = tr.find('td', {'width' :'274'}).text
                # print(extension)
                file_info = {'extension':extension,
                            'signature':signature,
                            'description':description}
                files_sign_list.append(file_info)
        else:
            print(f"요청 실패: {page.status_code}")
    return files_sign_list

if __name__ == '__main__':
    file_ext_list = get_file_extension_list()
    pprint.pprint(file_ext_list)