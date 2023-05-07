import requests
import re

def makeRequest(ip,fields):

    r = requests.get(f"http://ip-api.com/json/{ip}?fields={fields}")

    json = r.json()

    return json

def checkCity(ip,blockedCities):
    city = makeRequest(ip,fields="city")

    if city["city"] == "":
        return False

    for i in blockedCities:
        if city["city"].lower() == i.lower():
            return False

        else:
            return True


def checkCountry(ip,blockedCountries):
    country = makeRequest(ip,fields="countryCode")

    if country["countryCode"] == "":
        return False

    for i in blockedCountries:
        if country["countryCode"].lower() == i.lower():
            return False

        else:
            return True


def checkIpAddresses(ip,blockedIpAddresses):
    ip = makeRequest(ip,fields="query")

    for i in blockedIpAddresses:
        if ip["query"].lower() == i.lower():
            return False

        else:
            return True


def checkUserAgent(userAgent):
    payload = r'^(googlebot|bot|googlebot-mobile|googlebot-image|google favicon|mediapartners-google|bingbot|slurp|java|wget|curl|commons-httpclient|python-requests|python-urllib|libwww|httpunit|nutch|phpcrawl|msnbot|jyxobot|fast-webcrawler|fast enterprise crawler|biglotron|teoma|convera|seekbot|gigablast|exabot|ngbot|ia_archiver|gingercrawler|webmon |httrack|webcrawler|grub.org|usinenouvellecrawler|antibot|netresearchserver|speedy|fluffy|bibnum.bnf|findlink|msrbot|panscient|yacybot|aisearchbot|ioi|ips-agent|tagoobot|mj12bot|dotbot|woriobot|yanga|buzzbot|mlbot|yandexbot|purebot|linguee bot|voyager|cyberpatrol|voilabot|baiduspider|citeseerxbot|spbot|twengabot|postrank|turnitinbot|scribdbot|page2rss|sitebot|linkdex|adidxbot|blekkobot|ezooms|dotbot|mail.ru_bot|discobot|heritrix|findthatfile|europarchive.org|nerdbynature.bot|sistrix crawler|ahrefsbot|aboundex|domaincrawler|wbsearchbot|summify|ccbot|edisterbot|seznambot|ec2linkfinder|gslfbot|aihitbot|intelium_bot|facebookexternalhit|yeti|retrevopageanalyzer|lb-spider|sogou|lssbot|careerbot|wotbox|wocbot|ichiro|duckduckbot|lssrocketcrawler|drupact|webcompanycrawler|acoonbot|openindexspider|gnam gnam spider|web-archive-net.com.bot|backlinkcrawler|coccoc|integromedb|content crawler spider|toplistbot|seokicks-robot|it2media-domain-crawler|ip-web-crawler.com|siteexplorer.info|elisabot|proximic|changedetection|blexbot|arabot|wesee:search|niki-bot|crystalsemanticsbot|rogerbot|360spider|psbot|interfaxscanbot|lipperhey seo service|cc metadata scaper|g00g1e.net|grapeshotcrawler|urlappendbot|brainobot|fr-crawler|binlar|simplecrawler|livelapbot|twitterbot|cxensebot|smtbot|bnf.fr_bot|a6-indexer|admantx|facebot|twitterbot|orangebot|memorybot|advbot|megaindex|semanticscholarbot|ltx71|nerdybot|xovibot|bubing|qwantify|archive.org_bot|applebot|tweetmemebot|crawler4j|findxbot|semrushbot|yoozbot|lipperhey|y!j-asr|domain re-animator bot|addthis)'

    regex = r'^(mozilla|opera|chrome|safari|internet explorer)\/\d{1,10}\.\d{1,10}'

    regexCheck = re.compile(regex)
    payloadCheck = re.compile(payload)

    if not regexCheck.search(userAgent.lower()):

        return False
    
    if payloadCheck.search(userAgent.lower()):

        return False


    return True
    

def checkAsn(ip):
    asn = makeRequest(ip,fields="as")

    regex = r'^(google|microsoft|apple|bot)'

    if asn["as"] == "":
        return False
    
    r = re.compile(regex)

    if r.search(asn["as"].lower()):
        return False
    
    return True




def mainFunc(ip,userAgent,**kwargs):

    if "blockedIpAddresses" in kwargs.keys():
        check = checkIpAddresses(ip,kwargs["blockedIpAddresses"])

        if check == False:
            return False
    
    if "blockedCities" in kwargs.keys():
        check = checkCity(ip,kwargs["blockedCities"])

        if check == False:
            return False
    
    if "blockedCountries" in kwargs.keys():
        check = checkCountry(ip,kwargs["blockedCountries"])

        if check == False :
            return False
        



    if checkUserAgent(userAgent) == False:
        return False
    
    
    if checkAsn(ip) == False:
        return False

    


    return True
    
