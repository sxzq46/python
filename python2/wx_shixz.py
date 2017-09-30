#!/usr/bin/python

import json
import sys
import urllib
import urllib2
import time

def log(msg):
    try:
        with open("F:\\tmp\\wx.log", 'a') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
            f.write(" ")
            f.write(msg)
            f.write("\n")
    except Exception as e:
        with open("F:\\tmp\\wx.log", 'a') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
            f.write(" ")
            f.write("write log error %s" % str(e))
            f.write("\n")

def __init__():
    corpid = "wxeb3717fade5c3c92"
    corpsecret = "5_RDJyQvjbHPYW2fQP-jkS7TPtjvEgnJGaidyVsNLek2dtXrb_DJMLENDTODR-07"
    variable ={}
    variable["corpid"] = corpid
    variable["corpsecret"] = corpsecret
    return variable

def init_text(content):
    send_content ={
        "touser": "@all",
        "toparty": "5",
        "totag": "",
        "msgtype": "text",
        "agentid": "4",
        "text": {
        "content": "Hi Morning"
    },
    "safe":"0"
    }
    content = content
    send_content["text"]["content"] = content
    return send_content

def get_access_token():
    variable = __init__()
    data = urllib.urlencode(variable)
    req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/gettoken?%s' % data)
    response = urllib2.urlopen(req)
    r = response.read()
    print "Accessing %s?%s" % (req.get_full_url(), data)
    log("Accessing %s?%s" % (req.get_full_url(), data))
    return json.loads(r)

if __name__ == "__main__":
    log("start")
    text = init_text(sys.argv[3])
    log(text)
    js = get_access_token()
    if "errcode" in js:
        print "Can not get the access_token"
        log("Can not get the access_token")
        quit()
    access_token = js["access_token"]
    expires_in = js["expires_in"]
    data = json.dumps(text, ensure_ascii=False)
    req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token, data)
    response = urllib2.urlopen(req)
    r = response.read()
    result = json.loads(r)
    if result["errcode"] == 0:
        print "Sent successfully"
        log("Sent successfully")
    else:
        print result["errmsg"]
        log(result["errmsg"])
    log("stop")
