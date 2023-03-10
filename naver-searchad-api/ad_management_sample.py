import time
import random
import requests

import signaturehelper


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


BASE_URL = 'https://api.searchad.naver.com'
API_KEY = '010000000068f05de9b74812219e17267cc6b9f99112497b70742f2f176b03388c4f0d56f3'
SECRET_KEY = 'AQAAAABo8F3pt0gSIZ4XJnzGufmRRPHExa8r09mJY+cgOdiBYw=='
CUSTOMER_ID = '2802603'

# ManageCustomerLink Usage Sample

uri = '/customer-links'
method = 'GET'
r = requests.get(BASE_URL + uri, params={'type': 'MYCLIENTS'}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))


# BusinessChannel Usage Sample

uri = '/ncc/channels'
method = 'GET'
r = requests.get(BASE_URL + uri, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))


# Adgroup Usage Sample

# # 1. GET adgroup Usage Sample

uri = '/ncc/adgroups'
method = 'GET'
r = requests.get(BASE_URL + uri, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))
target_adgroup = r.json()[0]

# 2. CREATE adgroup Usage Sample

uri = '/ncc/adgroups'
method = 'POST'
payload = {'name': 'TEST#' + str(random.randrange(1000, 9999)), 'nccCampaignId' : target_adgroup['nccCampaignId'], 'pcChannelId' : target_adgroup['pcChannelId'], 'mobileChannelId': target_adgroup['mobileChannelId']}
r = requests.post(BASE_URL + uri, json=payload, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

created_adgroup = r.json()

# 3. UPDATE Adgroup Usage Sample

uri = '/ncc/adgroups/' + created_adgroup['nccAdgroupId']
method = 'PUT'
created_adgroup['userLock'] = 0
r = requests.put(BASE_URL + uri, params={'fields': 'userLock'}, json=created_adgroup, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

# 4. DELETE Adgroup

uri = '/ncc/adgroups/' + created_adgroup['nccAdgroupId']
method = 'DELETE'
r = requests.delete(BASE_URL + uri, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.content))

# AdKeyword Usage Sample

# 1. CREATE AdKeyword

uri = '/ncc/keywords'
method = 'POST'
r = requests.post(BASE_URL + uri, params={'nccAdgroupId': created_adgroup['nccAdgroupId']}, json=[{'keyword': 'hello'}], headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

created_adkeyword = r.json()[0]

# 2. GET AdKeyword

uri = '/ncc/keywords'
method = 'GET'
r = requests.get(BASE_URL + uri, params={'nccAdgroupId': created_adgroup['nccAdgroupId']}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

# 3. UPDATE AdKeyword

uri = '/ncc/keywords'
method = 'PUT'
created_adkeyword['userLock'] = 0
r = requests.put(BASE_URL + uri, params={'fields': 'userLock'}, json=[created_adkeyword], headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))


# 4. GET and UPDATE AdKeyword (BidAmt)

uri = '/ncc/keywords/' + created_adkeyword['nccKeywordId']
method = 'GET'
r = requests.get(BASE_URL + uri, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

retrieved_adkeyword = r.json()

uri = '/ncc/keywords'
method = 'PUT'
retrieved_adkeyword['bidAmt'] = 300
retrieved_adkeyword['useGroupBidAmt'] = 0
r = requests.put(BASE_URL + uri, params={'fields': 'bidAmt'}, json=[retrieved_adkeyword], headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))


# 5. DELETE AdKeyword

uri = '/ncc/keywords/' + created_adkeyword['nccKeywordId']
method = 'DELETE'
r = requests.delete(BASE_URL + uri, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.content))


# Estimate Usage Sample

# 1. average-position-bid

uri = '/estimate/average-position-bid/keyword'
method = 'POST'
r = requests.post(BASE_URL + uri, json={'device': 'PC', 'items': [{'key': '????????????', 'position': 1}, {'key': '??????????????????', 'position': 2}, {'key': '???????????????', 'position': 3}]}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("#response status_code = {}".format(r.status_code))
print("#response body = {}".format(r.json()))


# 2. exposure-minimum-bid

uri = '/estimate/exposure-minimum-bid/keyword'
method = 'POST'
r = requests.post(BASE_URL + uri, json={'device': 'PC', 'period': 'MONTH', 'items': ['????????????', '??????????????????', '???????????????']}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

# 3. median-bid

uri = '/estimate/median-bid/keyword'
method = 'POST'
r = requests.post(BASE_URL + uri, json={'device': 'PC', 'period': 'MONTH', 'items': ['????????????', '??????????????????', '???????????????']}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))


# 4. performance

uri = '/estimate/performance/keyword'
method = 'POST'
r = requests.post(BASE_URL + uri, json={'device': 'PC', 'keywordplus': True, 'key': '?????????', 'bids': [100, 500, 1000, 1500, 2000, 3000, 5000]}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

# 5. performance-bulk

uri = '/estimate/performance-bulk'
method = 'POST'
r = requests.post(BASE_URL + uri, json={'items': [{'device': 'PC', 'keywordplus': True, 'keyword': '????????????', 'bid': 70}, {'device': 'PC', 'keywordplus': True, 'keyword': '?????????', 'bid': 80}, {'device': 'PC', 'keywordplus': True, 'keyword': '???????????????', 'bid': 90}, ]}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))

# Stat Usage Sample

# 1. GET Summary Report per multiple entities 

uri = '/stats'
method = 'GET'
stat_ids = ['cmp-a001-01-000000006363279']
r = requests.get(BASE_URL + uri, params={'ids': stat_ids, 'fields': '["clkCnt","impCnt","salesAmt", "ctr", "cpc", "avgRnk", "ccnt"]', 'datePreset': 'yesterday'}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))
print("response body = {}".format(r.json()))
