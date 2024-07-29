import time
import requests
import json

cookies = {
    'qgqp_b_id': 'f6bc027cbaa355fde15eb80a2529d8ab',
    'websitepoptg_api_time': '1722088721785',
    'st_si': '15397080282946',
    'HAList': 'ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC',
    'st_asi': 'delete',
    'st_pvi': '34348567881173',
    'st_sp': '2024-07-27%2021%3A58%3A41',
    'st_inirUrl': 'https%3A%2F%2Fwww.google.com%2F',
    'st_sn': '12',
    'st_psi': '20240727220647420-113300300814-0398133831',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'qgqp_b_id=f6bc027cbaa355fde15eb80a2529d8ab; websitepoptg_api_time=1722088721785; st_si=15397080282946; HAList=ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC; st_asi=delete; st_pvi=34348567881173; st_sp=2024-07-27%2021%3A58%3A41; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=12; st_psi=20240727220647420-113300300814-0398133831',
    'Referer': 'https://data.eastmoney.com/zjlx/list.html',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_all_data_json():
    # 初始化数据
    data = []
    # 循环爬取
    for page in range(1, 58):
        time.sleep(0.5)  # 延迟爬取
        response = requests.get(
            'https://push2.eastmoney.com/api/qt/clist/get?fid=f184&po=1&pz=50&pn={}&np=1&fltt=2&invt=2&fields=f2%2Cf3%2Cf12%2Cf13%2Cf14%2Cf62%2Cf184%2Cf225%2Cf165%2Cf263%2Cf109%2Cf175%2Cf264%2Cf160%2Cf100%2Cf124%2Cf265%2Cf1&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2'
            .format(page),
            cookies=cookies,
            headers=headers,
        )
        # 追加数据
        data.append(json.loads(response.text))
        # 进度可视化
        print('爬取进度：{}/57'.format(page, ))
    # 写入数据
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


get_all_data_json()
