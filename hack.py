import requests
import hashlib
import sys
def request_api_data(http):
    url="https://api.pwnedpasswords.com/range/" + http
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f"Erorr fetching {res.status_code}ch")
    return res
def pwned_api_checker(password):
    shap1_password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5,tail=shap1_password[:5],shap1_password[5:]
    respon=request_api_data(first5)
    return get_password_leaks_count(respon,tail)
def get_password_leaks_count(response,passtocheck):
    hashes=(line.split(":") for line in response.text.splitlines())
    for hash in hashes:
        if hash[0]==passtocheck:
            return hash[1]
    return 0 
def main(args):
    count=pwned_api_checker(args)
    if count:
        return f"your password was found {count} time you should change youre password"
    else:
        return "your password was not found.carry on"