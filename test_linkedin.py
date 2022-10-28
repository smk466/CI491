from linkedin_search_people_scraper import *
linkedin.login_cookie(cookies=list_of_cookies)
true=True;false=False
list_of_cookies=[
{
    "domain": ".linkedin.com",
    "expirationDate": 1676463230,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1029585723.1610264105",
    "id": 1
}]
#please replace the above sample cookies with your cookies, can see below link of how to fetch cookies
linkedin.search_people(keyword='hr')
response=linkedin.people_results()
data=response['body']
#data=[{"Link": "https://www.linkedin.com/in/eram-khan-825112163?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BHEouHQrmSNy3NNHJ61sR5g%3D%3D"},..]