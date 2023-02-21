# api-bridge-jm

* naver-searchad-api : 네이버 검색 광고 API

  * ns-api-swagger.yaml : SWAGGER API로 API를 확인할 수 있습니다.
  * ns-test.ipynb : ipynb 형식으로 각 api 별 코드와 결과를 확인할 수 있습니다. 
  * ad_management_sample.py: 네이버 검색광고 공식 github 예제


# 네이버 검색 광고 API 목록

## base config

```python
BASE_URL = 'https://api.searchad.naver.com'
API_KEY = '<개인 api>'
SECRET_KEY = '<개인 secret_key>'
CUSTOMER_ID = '<customer_id>'
```

## Reference
네이버 검색 광고 api docs  : http://naver.github.io/searchad-apidoc/#/guides

---

## API 구조

    * 자세한 API request, response는 swagger.yaml에 작성해두었습니다. 

### 광고계정 > 캠페인 > 광고그룹(세트) > 광고 및 소재, 타겟 세그먼트의 성과 데이터 추출

1. 광고 계정
    각 광고 계정의 access Key를 직접 입력해야 함

2. 캠페인
   * GET /ncc/campaigns
        
        CustomId 별로 현재 진행중인 Campaigns 전부 가져오기
   
   * GET /ncc/campaigns/{campaignId}
    
        CampaignId 활용하여 Get

3. 광고그룹
    * GET /ncc/adgroups 
    
        CampaignId 활용하여 Get
    
    * GET /ncc/adgroups/{adgroupsId}

        CustomId 별로 현재 진행중인 Campaigns 전부 가져오기

    **Adgroup을 통해서 CampaignId, AdGroupId를 얻을 수 있는데 이 Id 가 앞으로 Ad, Stat 에서 사용되기 때문에 반드시 필요하다고 생각됩니다.**

4. 광고 및 소재, 타겟 세그먼트의 형식

    광고 API

    * GET /ncc/ads{?ids}

        ids : AdgroupId, IDs of the ad

        결과 adId를 반환합니다. 


    클릭, 노출 등등 확인하는 Api

    * Get /Stats/{ids,fields,datePreset}
    
        ids : campaign id, adGroup id, Ad keyword id, Ad id, Criterion id

        Stats를 통해서 campaign별, adGroup별, Ad 별 데이터를 확인할 수 있습니다.

    * Get /ncc/keywords{ids}

        ids : KeywordId
        KeywordIds가 필요하기 때문에 이를 구해오는 api를 찾아야한다. 

**따라서 그룹, 캠페인, 광고 API를 통해 각각의 ID를 받고 최종적으로 ID별로 Stat request를 보내서 데이터를 확인하는 구조입니다.**

--- 

### 캠페인, 광고그룹, 광고 별 Pause 기능 API

1. 캠페인 

    * PUT /ncc/campaigns/{campaignId} 

        campaignId : The unique ID of the Campaign.
        
        request body
        * userLock : Pause 여부

2. 광고그룹

    * PUT /ncc/adgroups/{adgroupId}

        adgroupId : The unique ID of the Ad Group.

        request body
        * userLock : Pause 여부

3. 광고
   
   * PUT /ncc/ads/{adId}

        adId : ID of the ad

        request body
        * userLock : Pause 여부


# 카카오 모먼트 api 목록


## base config

개인 access token : lsiF6WZrKCloFQsfjnvb6kgFarAtTSD32v4bZkoOCj1zFwAAAYZtuKp4

## Reference

카카오 모먼트 광고 api docs : https://developers.kakao.com/docs/latest/ko/kakaomoment/common

## API 구조

**광고계정 > 캠페인 > 광고그룹(세트) > 광고 및 소재, 타겟 세그먼트의 형식**

광고 계정 
