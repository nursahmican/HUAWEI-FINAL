import requests
from .apig_sdk import signer


def modelart(image_path): 
    
    url = "https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/f38d4ba6-3a56-439a-ab22-0f24d46e6474"
    ak = "BKW4VKQNXPJNICBKZ88G"
    sk = "P3TBOPPIdZrv4OisPUyLF9d6CK56WZMZErPzL1oE"
    
    method = 'POST'
    headers = {"x-sdk-content-sha256": "UNSIGNED-PAYLOAD"}
    request = signer.HttpRequest(method, url, headers)
    
    sig = signer.Signer()
    sig.Key = ak
    sig.Secret = sk
    sig.Sign(request)
    files = {'images': image_path}
    resp = requests.request(request.method, request.scheme + "://" + request.host + request.uri, headers=request.headers, files=files)
    
    
    return resp.text
    
