import json
import requests
import zlib

JAST_MAGIC_TOKEN = '0eb380773362e84a87c2c620712eb27b'
JAST_MAGIC_URL = 'https://api.just-magic.org/api_v1.php'


class JustMagic:
    def __init__(self, apiurl, apikey):
        self.apikey = apikey
        self.apiurl = apiurl

    def put_grp_onl(self, data, ya_lr):
        """
        Кластеризация семантики.
        На данном этапе только для регионов по Яндексу.
        data: список ключевиков через \n
        ya_lr: регион, можно указывать только 1 (default 213)
        """
        action = 'put_task'
        label = 'Задача от SalesBot'
        data = {'apikey': self.apikey,
                'action': action,
                'data': data,
                'ya_lr': ya_lr,
                'label': label,
                'task': 'grp_onl'}
        resp = requests.post(self.apiurl, data=data)
        if resp.status_code == 200:
            tid = int(json.loads(resp.text)['tid'])
            return tid

    def get_task_info(self, tid):
        """
        retutn: True - если таск запершен, False - если ещё выполняется.
        """
        action = 'get_task'
        data = {'apikey': self.apikey,
                'action': action,
                'mode': 'info',
                'tid': tid}
        resp = requests.post(self.apiurl, data=data)
        resp_json = json.loads(resp.text)
        err = resp_json.get('err')
        if err:
            return False
        elif resp_json.get('result').get('state') == 'fin':
            return True

    def get_grp_onl(self, tid):
        """
        return: список словарей, в каждом словаре - {название колонки: значение, ...}
        """
        action = 'get_task'
        data = {'apikey': self.apikey,
                'action': action,
                'mode': 'csv',
                'tid': tid,
                'system': 'unix'}
        resp = zlib.decompress(requests.post(JAST_MAGIC_URL, data=data).content, zlib.MAX_WBITS | 32).decode('utf-8')
        resp = [row.split('\t') for row in resp.split('\n') if row]
        resp_list = []
        for row in resp[1:]:
            row_dict = {}
            for idx, col in enumerate(row):
                row_dict[resp[0][idx]] = col
            resp_list.append(row_dict)
        return resp_list
