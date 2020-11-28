# -*- coding: utf-8 -*-
'''
Selfbot Edition

Special Thanks to:
 • Arifistifik
 • Team Newbie Corps™

Supported By:
 • We Bare Bears Corps™
 • B-G-N Squad

©2020 Recode By BAI
'''
from important import *
import youtube_dl
import requests
import humanize
import html5lib
from gtts import gTTS
from bs4 import BeautifulSoup
import requests, json
import urllib, urllib3, urllib.parse
from thrift import transport, protocol, server
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
parser = argparse.ArgumentParser(description='Selfbot By BAI')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
print ('##----- LOGIN CLIENT -----##')
line = LINE("Email","Pw")#Input Email & Pw Here
#=======================================================================================================================
myMid = line.profile.mid
programStart = time.time()
oepoll = OEPoll(line)
protectinvite = []
protectkick = []
protectjoin = []
protectqr = []
protectcancel = []
tmp_text = []
readers = {}
lurking = {}
settings = livejson.File('setting.json', True, False, 4)
ban = livejson.File('blacklist.json', True, False, 4)
silent = livejson.File('silent.json', True, False, 4)
tagmeOpen = codecs.open("tag.json","r","utf-8")

tagme = json.load(tagmeOpen)
lastseen = ({
    "find": {},
    "username": {}
})
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
wait = {
    "limit": 1,
    "wblacklist": False,
    "dblacklist": False,
    "wwhitelist": False,
    "dwhitelist": False,
}
liffV1 = {
    "arLiff": True
}
bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}
profile = line.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId
if not settings:
    print ('##----- LOAD DEFAULT JSON -----##')
    try:
        default_settings = line.server.getJson('https://17hosting.id/default.json')
        settings.update(default_settings)
        print ('##----- LOAD DEFAULT JSON (Success) -----##')
    except Exception:
        print ('##----- LOAD DEFAULT JSON (Failed) -----##')
def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))
def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd
def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')
def allowLiff3(): #LIFF TROJAN
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': line.authToken,
        'X-Line-Application': line.server.APP_NAME,
        'X-Line-ChannelId': '1638870522',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
def allowLiff2(): #LIFF EATER
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': line.authToken,
        'X-Line-Application': line.server.APP_NAME,
        'X-Line-ChannelId': '1586794970',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)         
def allowLiff(): #LIFF AR
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': line.authToken,
        'X-Line-Application': line.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
def sendTemplate(to, data):
    allowLiff()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    if liffV1["arLiff"]: view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    else: view = LiffViewRequest('1586794970-VKzbNLP7', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendTemplate3(to, data):
    allowLiff3()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1638870522-PnjreV13', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate2(to, data):
    allowLiff2()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1586794970-VKzbNLP7', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "We Bare Bears Coprs™",
            "iconUrl": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=u337c18ad01bdc582a952bbabe1832644"
        }
    }
    sendTemplate(to, data)
def changeProfileVideo(to):
	if settings['changeProfileVideo']['picture'] == None:
		return line.sendReplyMessage(msg.id, to,"「 Picture Not Found♪ 」")
	elif settings['changeProfileVideo']['video'] == None:
		return line.sendReplyMessage(msg.id, to,"「 Video Not Found♪ 」")
	else:
		path = settings['changeProfileVideo']['video']
		files = {'file': open(path, 'rb')}
		obs_params = line.genOBSParams({'oid': line.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
		data = {'params': obs_params}
		r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
		if r_vp.status_code != 201:
			return line.sendMessage(to,"「 Fail Update Profile♪ 」")
		path_p = settings['changeProfileVideo']['picture']
		settings['changeProfileVideo']['status'] = False
		line.updateProfilePicture(path_p, 'vp')
def changevideopp(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))
def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')
def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]
def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False
def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text
def help():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    help =   "╭───「 Help 」" + "\n" + \
             "├➢ Group" + "\n" + \
             "├➢ Remote" + "\n" + \
             "├➢ Kick" + "\n" + \
             "├➢ Spam" + "\n" + \
             "├➢ Setting" + "\n" + \
             "╰───「 We Bare Bears Corps™ 」"
    return help
def special():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGroup =   "╭───「 Help Group 」" + "\n" + \
                    "├➢ Groupinfo" + "\n" + \
                    "├➢ Grouplist" + "\n" + \
                    "├➢ InvitationList" + "\n" + \
                    "├➢ Invite「 Mention 」" + "\n" + \
                    "├➢ Reinvite「 Mention 」" + "\n" + \
                    "├➢ Xinvite「 Reply 」" + "\n" + \
                    "├➢ Openqr" + "\n" + \
                    "├➢ Closeqr" + "\n" + \
                    "├➢ Bl" + "\n" + \
                    "├➢ Wl" + "\n" + \
                    "├➢ Protect:set" + "\n" + \
                    "├➢ Protect:list" + "\n" + \
                    "├➢ Changegroupname「 Name 」" + "\n" + \
                    "├➢ Changegrouppict" + "\n" + \
                    "├➢ Lastseen「 Mention 」" + "\n" + \
                    "├➢ Find「 Mention 」" + "\n" + \
                    "├➢ Check mention" + "\n" + \
                    "├➢ Delcheckmention" + "\n" + \
                    "├➢ Mentionall" + "\n" + \
                    "╰───「 We Bare Bears Corps™ 」"
    return helpGroup
def helpsettings():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSettings =   "╭───「 Help Setting 」" + "\n" + \
                    "├➢ " + key + " AutoAdd「On/Off」" + "\n" + \
                    "├➢ " + key + " AutoJoin「On/Off」" + "\n" + \
                    "├➢ " + key + " AutoJoinTicket「On/Off」" + "\n" + \
                    "├➢ " + key + " AutoLeave「On/Off」" + "\n" + \
                    "├➢ " + key + " AutoRead「On/Off」" + "\n" + \
                    "├➢ " + key + " AutoRespon「On/Off」" + "\n" + \
                    "├➢ " + key + " CheckContact「On/Off」" + "\n" + \
                    "├➢ " + key + " CheckPost「On/Off」" + "\n" + \
                    "├➢ " + key + " CheckSticker「On/Off」" + "\n" + \
                    "├➢ " + key + " Unsend「On/Off」" + "\n" + \
                    "├➢ " + key + " Sider「On/Off」" + "\n" + \
                    "╰───「 We Bare Bears Corps™ 」"
    return helpSettings
def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result
def mentionMembers(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = '╭───[ Mention Members ]\n'
    mention = '@baiselfbot\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───[ We Bare Bears Corps™ ]\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
def mentionMembers2(gid, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    G = line.getGroup(gid)
    result = '╭───[ Remote Mention ]\n'
    mention = '@baiselfbot\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───[ We Bare Bears Corps™ ]\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendMessage(gid, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@baiselfbot "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def cloneProfile(mid):
    contact = line.getContact(mid)
    profile = line.getProfile()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile(profile)
    if contact.pictureStatus:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture(pict)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)
def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def debug():
	get_profile_time_start = time.time()
	get_profile = line.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\nType: Speed♪\n • Took : %.3fms♪\n • Taken: %.5f♪" % (get_profile_took,get_profile_time)
def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    line.updateProfile(profile)
    if settings['myProfile']['pictureStatus']:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'])
        line.updateProfilePicture(pict)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'mute':
        if to in silent['silent']:
            line.sendReplyMessage(msg.id, to, 'you have to Mute this group :)\nPlease Usage Commands "unmute" ')
        else:
            silent['silent'].append(to)
            line.sendReplyMessage(msg.id, to, 'Bot cant Not Operation again♪')
    elif cmd == 'unmute':
        if to not in silent['silent']:
            line.sendReplyMessage(msg.id, to, "you haven't  this group :)")
        else:
            silent['silent'].remove(to)
            line.sendReplyMessage(msg.id, to, 'Bot can Operation again♪')
    if to in silent['silent']:
        return
    if cmd == 'logout':
        line.sendMessage(to, 'Selfbot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    elif cmd == 'logoutdevicee':
        line.logout()
        sys.exit('##----- CLIENT LOGOUT -----##')
    elif cmd == 'restart':
        line.sendMessage(to, 'Bot will restarting, please wait until the bot can operate ♪')
        settings['restartPoint'] = to
        restartProgram()
#================Menu Help================
    elif cmd == 'help':
                    Help = help()
                    sendFooter(to,Help)
    elif cmd == 'group':
                    Group = special()
                    sendFooter(to,Group)
    elif cmd == 'setting':
                    helpSettings = helpsettings()
                    sendFooter(to,helpSettings)
    elif cmd == 'kick':
                    ret = "╭───「 Help Kick 」"
                    ret += "\n├➢ Kickall"
                    ret += "\n├➢ Cancelall"
                    ret += "\n├➢ Kick「 Mention 」"
                    ret += "\n├➢ Vkick「 Mention 」"
                    ret += "\n├➢ Mkick「 Mention 」"
                    ret += "\n├➢ Xkick「 Reply 」"
                    ret += "\n╰───「 We Bare Bears Corps™ 」"
                    sendFooter(to,ret)
    elif cmd == 'bl':
                    ret = "╭───「 Help Blacklist 」"
                    ret += "\n├➢ blacklist"
                    ret += "\n├➢ clearbl"
                    ret += "\n├➢ detectbl"
                    ret += "\n├➢ addbl「 Mention 」"
                    ret += "\n├➢ debl「 Mention 」"
                    ret += "\n├➢ bl:「 On/Off 」"
                    ret += "\n├➢ unbl「 Num 」"
                    ret += "\n╰───「 We Bare Bears Corps™ 」"
                    sendFooter(to,ret)
    elif cmd == 'wl':
                    ret = "╭───「 Help Whitelist 」"
                    ret += "\n├➢ whitelist"
                    ret += "\n├➢ clearwl"
                    ret += "\n├➢ detectwl"
                    ret += "\n├➢ addwl「 Mention 」"
                    ret += "\n├➢ dewl「 Mention 」"
                    ret += "\n├➢ wl:「 On/Off 」"
                    ret += "\n├➢ unwl「 Num 」"
                    ret += "\n╰───「 We Bare Bears Corps™ 」"
                    sendFooter(to,ret)
    elif cmd == 'remote':
                    ret = "╭───「 Help Remote 」"
                    ret += "\n├➢ .openqr 「 Num 」"
                    ret += "\n├➢ .closeqr 「 Num 」"
                    ret += "\n├➢ .ginfo「 Num 」"
                    ret += "\n├➢ .infomem「 Num 」"
                    ret += "\n├➢ .mentionall 「 Num 」"
                    ret += "\n├➢ .unsend 「 Num 」「 Numb 」"
                    ret += "\n├➢ .spamcall 「 Num 」「 Numb 」"
                    ret += "\n╰───「 We Bare Bears Corps™ 」"
                    sendFooter(to,ret)
    elif cmd == 'spam':
                    ret = "╭───「 Help Spam 」"
                    ret += "\n├➢ Spamcall「 Num 」"
                    ret += "\n├➢ Spamcallto「Num」「Mention」"
                    ret += "\n├➢ Spamtag「Num」「Mention」"
                    ret += "\n├➢ Spamtext「Num」「Text」"
                    ret += "\n╰───「 We Bare Bears Corps™ 」"
                    sendFooter(to,ret)
#================BATAS================
    elif cmd == 'speed':
            debugs = debug()
            sendFooter(to,debugs)
    elif cmd == 'me':
        line.sendMessageMusic(to, title=line.getContact(myMid).displayName, subText=str(line.getContact(myMid).statusMessage), url='https://line.me/ti/p/~imsnowball', iconurl="http://dl.profile.line-cdn.net/{}".format(line.getContact(myMid).pictureStatus), contentMetadata={})
    elif cmd == 'runtime':
        runtime = time.time() - programStart
        sendFooter(to, 'Bot already running on ' + format_timespan(runtime))
    elif cmd == 'creator':
        line.sendContact(to, 'u337c18ad01bdc582a952bbabe1832644')
    elif cmd == 'cekbot':
        try:line.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
        except:has = "NOT"
        try:line.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
        except:has1 = "NOT"
        try:line.cancelGroupInvitation(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has2 = "OK"
        except:has2 = "NOT"
        idbob = line.getProfile().userid
        try:line.findContactsByUserid(idbob);has3 = "OK"
        except:has3 = "NOT"
        if has == "OK":sil = "Normal"
        else:sil = "Limit"
        if has1 == "OK":sil1 = "Normal"
        else:sil1 = "Limit"
        if has2 == "OK":sil2 = "Normal"
        else:sil2 = "Limit"
        if has3 == "OK":sil3 = "Normal"
        else:sil3 = "Limit"
        ret_ = "╭───[ Check Limit ]"
        ret_ += "\n├➢ Kick: {}".format(sil1)
        ret_ += "\n├➢ Invite: {}".format(sil)
        ret_ += "\n├➢ Cancel: {}".format(sil2)
        ret_ += "\n├➢ Add: {}".format(sil3)
        ret_ += "\n╰───[ We Bare Bears Corps™ ]"
        sendFooter(to,ret_)
    elif cmd == "byeme":
        text = "See You Again"
        sendFooter(to,text)
        G = line.getGroup(to)
        line.leaveGroup(to)
#================FOR USE VPS (VIRTUAL PRIVAT SERVER)================
    if cmd == "memory":
            am = subprocess.getoutput('cat /proc/meminfo')
            core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
            for anu in am.splitlines():
                if 'MemTotal:' in anu:
                    mem = anu.split('MemTotal:')[1].replace(' ','')
                if 'MemFree:' in anu:
                    fr = anu.split('MemFree:')[1].replace(' ','')
            res = '╭───[ Memory ]'
            res += "\n├➢ Cpu Core : {}".format(core)
            res += "\n├➢ Total Memory: {}".format(mem)
            res += "\n├➢ Free Memory: {}".format(fr)
            res += '\n╰───[ We Bare Bears Corps™ ]'
            sendFooter(to,res)
    elif cmd == "clears":
            a = os.popen('echo 1 | sudo tee /proc/sys/vm/drop_caches\necho 2 | sudo tee /proc/sys/vm/drop_caches\necho 3 | sudo tee /proc/sys/vm/drop_caches\n').read()
            b = os.popen('cd / && cd tmp && rm *.bin').read()
            res = "Success clear cache Vps"
            sendFooter(to, res)
#================Blacklist & Whitelist================
    elif cmd.startswith("addwl "):
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            targets = []
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            for target in targets:
                try:
                    settings["whitelist"].append(target)
                    line.sendReplyMentionV2(msg_id,to,"「 Add Whitelist 」\nUser @! Added To Whitelist",[target])
                except:
                    pass
    elif cmd.startswith("delwl "):
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            targets = []
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            for target in targets:
                try:
                    settings["whitelist"].remove(target)
                    line.sendReplyMentionV2(msg_id,to,"「 Delete Whitelist 」\nUser @! Deleted To Whitelist",[target])
                except:
                    pass
    elif cmd.startswith("addbl "):
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            targets = []
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            for target in targets:
                try:
                    ban["blacklist"].append(target)
                    line.sendReplyMentionV2(msg_id,to,"「 Add Blacklist 」\nUser @! Added To Blacklist",[target])
                except:
                    pass
    elif cmd.startswith("delbl "):
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            targets = []
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            for target in targets:
                try:
                    ban["blacklist"].remove(target)
                    line.sendReplyMentionV2(msg_id,to,"「 Delete Blacklist 」\nUser @! Deleted To Blacklist",[target])
                except:
                    pass 
    elif cmd == 'blacklist':
						if len(ban["blacklist"]) > 0:
							h = [a for a in ban["blacklist"]]
							k = len(h)//20
							for aa in range(k+1):
								if aa == 0:dd = '╭───[ Blacklist ]';no=aa
								else:dd = '';no=aa*20
								msgas = dd
								for a in h[aa*20:(aa+1)*20]:
									no+=1
									if no == len(h):msgas+='\n├➢ {}. @!\n╰───[ We Bare Bears Corps™ ]'.format(no)
									else:msgas += '\n├➢ {}. @!'.format(no)
								sendMention(to, msgas, h[aa*20:(aa+1)*20])
						else:
							sendFooter(to,"「 Doesn't Have Any Blacklist User -_- 」")
    elif cmd == 'whitelist':
						if len(settings["whitelist"]) > 0:
							h = [a for a in settings["whitelist"]]
							k = len(h)//20
							for aa in range(k+1):
								if aa == 0:dd = '╭───[ Whitelist ]';no=aa
								else:dd = '';no=aa*20
								msgas = dd
								for a in h[aa*20:(aa+1)*20]:
									no+=1
									if no == len(h):msgas+='\n├➢ {}. @!\n╰───[ We Bare Bears Corps™ ]'.format(no)
									else:msgas += '\n├➢ {}. @!'.format(no)
								sendMention(to, msgas, h[aa*20:(aa+1)*20])
						else:
							sendFooter(to,"「 Doesn't Have Any whitelist User -_- 」")
    elif cmd.startswith("unbl "):
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    blacklist = ban["blacklist"]
                                    bl = blacklist[int(number)-1]
                                    ban["blacklist"].remove(bl)
                                    sendFooter(to, "「 1 User Dihapus dalam blacklist 」")
    elif cmd.startswith("unwl "):
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    whitelist = settings["whitelist"]
                                    wl = whitelist[int(number)-1]
                                    settings["whitelist"].remove(wl)
                                    sendFooter(to, "「 1 User Dihapus dalam whitelist 」")
    elif cmd == 'clearbl':
						if len(ban["blacklist"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} User Dihapus dalam blacklist 」".format(len(ban["blacklist"])))
							ban["blacklist"].clear()
						else:
							sendFooter(to,"「 Tidak Ada Blacklist User -_- 」")
    elif cmd == 'clearwl':
						if len(settings["whitelist"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} User Dihapus dalam whitelist 」".format(len(settings["whitelist"])))
							settings["whitelist"].clear()
						else:
							sendFooter(to,"「 Tidak Ada whitelist User -_- 」")
    elif cmd == "bl:on":
                                wait["wblacklist"] = True
                                sendFooter(to,"「 Blacklist 」\nPlease Send Contact To Add ^_^")

    elif cmd == "bl:off":
                                wait["dblacklist"] = True
                                sendFooter(to,"「 Blacklist 」\nPlease Send Contact To Delete ^_^")
    elif cmd == "wl:on":
                                wait["wwhitelist"] = True
                                sendFooter(to,"「 Whitelist 」\nPlease Send Contact To Add ^_^")

    elif cmd == "wl:off":
                                wait["dwhitelist"] = True
                                sendFooter(to,"「 Whitelist 」\nPlease Send Contact To Delete ^_^")
    elif cmd == "detectbl":
                        if msg.toType == 2:
                            group = line.getGroup(to)
                            nama = [contact.mid for contact in group.members]
                            lists = []
                            for tag in ban["blacklist"]:
                                lists+=filter(lambda str: str == tag, nama)
                            if lists == []:
                                line.sendReplyMessage(msg.id, to, "「 Blacklist Not Detect 」")
                                return
                            if len(lists) > 0: 
                                h = [a for a in lists]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '╭───[ Detect Blacklist ]';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if no == len(h):msgas+='\n├➢ {}. @!\n│• Blacklist Detect!!\n│• Be CareFull\n╰───[ We Bare Bears Corps™ ]'.format(no)
                                        else:msgas += '\n├➢ {}. @!'.format(no)
                                    sendMention(to, msgas, h[aa*20:(aa+1)*20])
    elif cmd == "detectwl":
                        if msg.toType == 2:
                            group = line.getGroup(to)
                            nama = [contact.mid for contact in group.members]
                            lists = []
                            for tag in settings["whitelist"]:
                                lists+=filter(lambda str: str == tag, nama)
                            if lists == []:
                                line.sendReplyMessage(msg.id, to, "「 Whitelist Not Detect 」")
                                return
                            if len(lists) > 0: 
                                h = [a for a in lists]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '╭───[ Detect Whitelist ]';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if no == len(h):msgas+='\n├➢ {}. @!\n│• Whitelist Detect!!\n╰───[ We Bare Bears Corps™ ]'.format(no)
                                        else:msgas += '\n├➢ {}. @!'.format(no)
                                    sendMention(to, msgas, h[aa*20:(aa+1)*20])
#================Protection================
    elif cmd == "protect:set":
                                md = "┏━━━「 Status Protected 」\n"
                                if msg.to in settings["protectqr"]: md+="┣ QR Protection 「🔒」\n"
                                else: md+="┣ QR Protection 「🔓」\n"
                                if msg.to in settings["protectjoin"]: md+="┣ Lock Join 「🔒」\n"
                                else: md+="┣ Lock Join 「🔓」\n"
                                if msg.to in settings["protectkick"]: md+="┣ Lock Kick 「🔒」\n"
                                else: md+="┣ Lock Kick 「🔓」\n"
                                if msg.to in settings["protectinvite"]: md+="┣ Deny Invitation 「🔒」\n"
                                else: md+="┣ Deny Invitation 「🔓」\n"
                                if msg.to in settings["protectcancel"]: md+="┣ Lock Cancel 「🔒」"
                                else: md+="┣ Lock Cancel 「🔓」"
                                ret_ = str(md)
                                ret_ += "\n┣━━「 Protect Command 」"
                                ret_ += "\n┣ lock:qr「 On/Off 」"
                                ret_ += "\n┣ lock:join「 On/Off 」"
                                ret_ += "\n┣ lock:kick「 On/Off 」"
                                ret_ += "\n┣ deny:invite「 On/Off 」"
                                ret_ += "\n┣ lock:cancel「 On/Off 」"
                                ret_ += "\n┣ max:protection「 On/Off 」"
                                ret_ += "\n┣━━「 Symbol Details 」"
                                ret_ += "\n┣「🔒」: On/True/Enabled"
                                ret_ += "\n┣「🔓」: Off/False/Disabled"
                                ret_ += "\n┗━━━「 We Bare Bears Corps™ 」"
                                sendFooter(to,ret_)
    elif cmd == 'clear lock:join':
						if len(settings["protectjoin"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} List Cleared All Lock Join 」".format(len(settings["protectjoin"])))
							settings["protectjoin"].clear()
						else:
							sendFooter(to,"「 Doesn't List Lock Join -_- 」")
    elif cmd == 'clear lock:kick':
						if len(settings["protectkick"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} Clear List Cleared All Lock Kick 」".format(len(settings["protectkick"])))
							settings["protectkick"].clear()
						else:
							sendFooter(to,"「 Doesn't List Lock Kick -_- 」")
    elif cmd == 'clear deny:invite':
						if len(settings["protectinvite"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} Clear List Cleared All Deny Invitation 」".format(len(settings["protectinvite"])))
							settings["protectinvite"].clear()
						else:
							sendFooter(to,"「 Doesn't List Deny Invitation -_- 」")
    elif cmd == 'clear lock:cancel':
						if len(settings["protectcancel"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} Clear List Cleared All Lock Cancel 」".format(len(settings["protectcancel"])))
							settings["protectcancel"].clear()
						else:
							sendFooter(to,"「 Doesn't List Lock Cancel -_- 」")
    elif cmd == 'clear lock:qr':
						if len(settings["protectqr"]) > 0:
							line.sendReplyMessage(msg.id, to, "「 {} Clear List Cleared All QR Protection 」".format(len(settings["protectqr"])))
							settings["protectqr"].clear()
						else:
							sendFooter(to,"「 Doesn't List QR Protection -_- 」")					
    elif cmd == 'protect:list':
                                ma = ""
                                mb = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                d = 0
                                e = 0
                                f = 0
                                gid = settings["protectqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +line.getGroup(group).name + "\n"
                                gid = settings["protectkick"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +line.getGroup(group).name + "\n"
                                gid = settings["protectjoin"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +line.getGroup(group).name + "\n"
                                gid = settings["protectinvite"]
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +line.getGroup(group).name + "\n" 
                                gid = settings["protectcancel"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +line.getGroup(group).name + "\n"                                    
                                line.generateReplyMessage(msg.id)
                                line.sendReplyMessage(msg.id, to,"• Protectlist •\n\n- QR Protection :\n"+ma+"\n- Lock Kick :\n"+mb+"\n- Lock Join :\n"+md+"\n- Deny Invitation :\n"+me+"\n- Lock Cancel :\n"+mf+"\nTotal「%s」Protect Group\n\nWe Bare Bears Corps™" % (str(len(settings["protectqr"])+len(settings["protectkick"])+len(settings["protectjoin"])+len(settings["protectinvite"])+len(settings["protectcancel"]))))
    elif cmd.startswith("lock:kick "):
                            spl = cmd.replace("lock:kick ","")
                            if spl == 'on':
                                if msg.to in settings["protectkick"]:
                                     msgs = "Lock Kick Already Enabled -_-"
                                else:
                                     settings["protectkick"].append(msg.to)
                                     ginfo = line.getGroup(msg.to)
                                     msgs = "Lock Kick Enabled\nOn Group: " +str(ginfo.name)
                                line.sendReplyMessage(msg.id, to, "「 Lock Kick 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in settings["protectkick"]:
                                       settings["protectkick"].remove(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "Lock Kick Disabled\nOn Group: " +str(ginfo.name)
                                  else:
                                       msgs = "Lock Kick Already Disabled -_-"
                                  line.sendReplyMessage(msg.id, to, "「 Lock Kick 」\n" + msgs)
    elif cmd.startswith("deny:invite "):
                            spl = cmd.replace("deny:invite ","")
                            if spl == 'on':
                                if msg.to in settings["protectinvite"]:
                                     msgs = "Deny Invitation Already Enabled -_-"
                                else:
                                     settings["protectinvite"].append(msg.to)
                                     ginfo = line.getGroup(msg.to)
                                     msgs = "Deny Invitation Enabled\nOn Group: " +str(ginfo.name)
                                line.sendReplyMessage(msg.id, to, "「 Deny Invitation 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in settings["protectinvite"]:
                                       settings["protectinvite"].remove(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "Deny Invitation Disabled\nOn Group: " +str(ginfo.name)
                                  else:
                                       msgs = "Deny Invitation Already Disabled -_-"
                                  line.sendReplyMessage(msg.id, to, "「 Deny Invitation 」\n" + msgs)        
    elif cmd.startswith("lock:join "):
                            spl = cmd.replace("lock:join ","")
                            if spl == 'on':
                                if msg.to in settings["protectjoin"]:
                                     msgs = "Lock Join Already Enabled -_-"
                                else:
                                     settings["protectjoin"].append(msg.to)
                                     ginfo = line.getGroup(msg.to)
                                     msgs = "Lock Join Enabled\nOn Group: " +str(ginfo.name)
                                line.sendReplyMessage(msg.id, to, "「 Lock Join 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in settings["protectjoin"]:
                                       settings["protectjoin"].remove(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "Lock Join Disabled\nOn Group: " +str(ginfo.name)
                                  else:
                                       msgs = "Lock Join Already Disabled -_-"
                                  line.sendReplyMessage(msg.id, to, "「 Lock Join 」\n" + msgs)            
    elif cmd.startswith("lock:qr "):
                            spl = cmd.replace("lock:qr ","")
                            if spl == 'on':
                                if msg.to in settings["protectqr"]:
                                     msgs = "QR Lock Already Enabled -_-"
                                else:
                                     settings["protectqr"].append(msg.to)
                                     ginfo = line.getGroup(msg.to)
                                     msgs = "QR Lock Enabled\nOn Group: " +str(ginfo.name)
                                line.sendReplyMessage(msg.id, to, "「 QR Protection  」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in settings["protectqr"]:
                                       settings["protectqr"].remove(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "QR Lock Disabled\nOn Group: " +str(ginfo.name)
                                  else:
                                       msgs = "QR Lock Already Disabled -_-"
                                  line.sendReplyMessage(msg.id, to, "「 QR Protection  」\n" + msgs)               
    elif cmd.startswith("lock:cancel "):
                            spl = cmd.replace("lock:cancel ","")
                            if spl == 'on':
                                if msg.to in settings["protectcancel"]:
                                     msgs = "Lock Cancel Already Enabled -_-"
                                else:
                                     settings["protectcancel"].append(msg.to)
                                     ginfo = line.getGroup(msg.to)
                                     msgs = "Lock Cancel Enabled\nOn Group: " +str(ginfo.name)
                                line.sendReplyMessage(msg.id, to, "「 Lock Cancel 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in settings["protectcancel"]:
                                       settings["protectcancel"].remove(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "Lock Cancel Disabled\nOn Group: " +str(ginfo.name)
                                  else:
                                       msgs = "Lock Cancel Already Disabled -_-"
                                  line.sendReplyMessage(msg.id, to, "「 Lock Cancel 」\n" + msgs)
    elif cmd.startswith("max:protection "):
                            spl = cmd.replace("max:protection ","")
                            if spl == "on":
                                if msg.to in settings["protectkick"]:
                                     msgs = ""
                                else:
                                     settings["protectkick"].append(msg.to)
                                if msg.to in settings["protectqr"]:
                                     msgs = ""
                                else:
                                     settings["protectqr"].append(msg.to)
                                if msg.to in settings["protectjoin"]:
                                     msgs = ""
                                else:
                                     settings["protectjoin"].append(msg.to)
                                if msg.to in settings["protectcancel"]:
                                     msgs = ""
                                else:
                                     settings["protectcancel"].append(msg.to)
                                if msg.to in settings["protectinvite"]:
                                     msgs = "Maximum Protection Already Enabled"
                                else:
                                     settings["protectinvite"].append(msg.to)
                                     info = line.getGroup(msg.to)
                                     msgs = "Maximum Protection Enabled\nOn Group: " +str(info.name)
                                line.sendReplyMessage(msg.id, to, "「 Maximum Protection 」\n" + msgs)
                            if spl == "off":
                                if msg.to in settings["protectkick"]:
                                     settings["protectkick"].remove(msg.to)
                                     msgs = ""
                                else:
                                     msgs = ""
                                if msg.to in settings["protectinvite"]:
                                   settings["protectinvite"].remove(msg.to)
                                   msgs = ""
                                else:
                                   msgs = ""
                                if msg.to in settings["protectqr"]:
                                   settings["protectqr"].remove(msg.to)
                                   msgs = ""
                                else:
                                   msgs = ""
                                if msg.to in settings["protectjoin"]:
                                   settings["protectjoin"].remove(msg.to)
                                   msgs = ""
                                else:
                                   msgs = ""
                                if msg.to in settings["protectcancel"]:
                                   settings["protectcancel"].remove(msg.to)
                                   info = line.getGroup(msg.to)
                                   msgs = "Maximum Protection Disabled\nOn Group: " +str(info.name)
                                else:
                                   msgs = "Maximum Protection Already Disabled -_-"
                                line.sendReplyMessage(msg.id, to, "「 Maximum Protection 」\n" + msgs)
#================BATAS================
    elif cmd == 'about':
        res = '╭───[ About ]'
        res += '\n├➢ Type : Selfbot'
        res += '\n├➢ Version : 4.5.0'
        res += '\n├➢ Library : linepy (Python)'
        res += '\n├➢ Creator : Bobby'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        sendFooter(to, res)
    elif cmd == 'status':
        res = '╭───[ Status ]'
        res += '\n├➢ Auto Like : ' + bool_dict[settings['autolike']][1]
        res += '\n├➢ Auto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├➢ Auto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├➢ Auto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├➢ Auto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├➢ Auto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\n├➢ Setting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├➢ Mimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├➢ Mention Kick : ' + bool_dict[settings['mentionkick']][1]
        res += '\n├➢ Greetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├➢ Greetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\n├➢ Check Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\n├➢ Check Post : ' + bool_dict[settings['checkPost']][1]
        res += '\n├➢ Check Sticker : ' + bool_dict[settings['checkSticker']][1]
        res += '\n╰───[ We Bare Bears Corps™ ]'
        sendFooter(to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            sendFooter(to, 'Change group picture aborted')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            sendFooter(to, 'Change picture profile aborted')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            sendFooter(to, 'Change cover profile aborted')
            aborted = True
        if wait["wblacklist"]:
            wait["wblacklist"] = False
            sendFooter(to, 'Blacklist Contact aborted')
            aborted = True
        if wait["dblacklist"]:
            wait["dblacklist"] = False
            sendFooter(to, 'UnBlacklist Contact aborted')
            aborted = True
        if wait["wwhitelist"]:
            wait["wwhitelist"] = False
            sendFooter(to, 'Whitelist Contact aborted')
            aborted = True
        if wait["dwhitelist"]:
            wait["dwhitelist"] = False
            sendFooter(to, 'UnWhitelist Contact aborted')
            aborted = True
        if not aborted:
            sendFooter(to, 'Failed abort, nothing to abort')
    elif cmd.startswith('error'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───[ Error ]'
        res += '\n├➢ Usage : '
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Error Logs'
        res += '\n│ • {key}Error Reset'
        res += '\n│ • {key}Error Detail <errid>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'error':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'logs':
            try:
                filee = open('errorLog.txt', 'r')
            except FileNotFoundError:
                return line.sendMessage(to, 'Failed display error logs, error logs file not found')
            errors = [err.strip() for err in filee.readlines()]
            filee.close()
            if not errors: return line.sendMessage(to, 'Failed display error logs, empty error logs')
            res = '╭───[ Error Logs ]'
            res += '\n├ List :'
            parsed_len = len(errors)//200+1
            no = 0
            for point in range(parsed_len):
                for error in errors[point*200:(point+1)*200]:
                    if not error: continue
                    no += 1
                    res += '\n│ %i. %s' % (no, error)
                    if error == errors[-1]:
                        res += '\n╰───[ We Bare Bears Corps™ ]'
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMessage(to, res)
                res = ''
        elif cond[0].lower() == 'reset':
            filee = open('errorLog.txt', 'w')
            filee.write('')
            filee.close()
            shutil.rmtree('tmp/errors/', ignore_errors=True)
            os.system('mkdir tmp/errors')
            line.sendMessage(to, 'Success reset error logs')
        elif cond[0].lower() == 'detail':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            errid = cond[1]
            if os.path.exists('tmp/errors/%s.txt' % errid):
                with open('tmp/errors/%s.txt' % errid, 'r') as f:
                    line.sendMessage(to, f.read())
            else:
                return line.sendMessage(to, 'Failed display details error, errorid not valid')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───[ Setting Key ]'
        res += '\n├➢ Status : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├➢ Key : ' + settings['setKey']['key'].title()
        res += '\n├➢ Usage : '
        res += '\n│ • Setkey'
        res += '\n│ • Setkey <on/off>'
        res += '\n│ • Setkey <key>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if txt == 'setkey':
            line.sendMessage(to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                line.sendMessage(to, 'Failed activate setkey, setkey already active')
            else:
                settings['setKey']['status'] = True
                line.sendMessage(to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                line.sendMessage(to, 'Failed deactivate setkey, setkey already deactive')
            else:
                settings['setKey']['status'] = False
                line.sendMessage(to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            line.sendMessage(to, 'Success change set key to (%s)' % textt)
    elif cmd == "antitag on":
        settings["mentionkick"] = True
        sendFooter(to, 'Success activated antitag')
    elif cmd == "antitag off":
        settings["mentionkick"] = False
        sendFooter(to, 'Success deactivated antitag')
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───[ Auto Add ]'
        res += '\n├➢ Status : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├➢ Reply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\n├➢ Reply Message : ' + settings['autoAdd']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}AutoAdd'
        res += '\n│ • {key}AutoAdd <on/off>'
        res += '\n│ • {key}AutoAdd Reply <on/off>'
        res += '\n│ • {key}AutoAdd <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'autoadd':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                line.sendMessage(to, 'Autoadd already active')
            else:
                settings['autoAdd']['status'] = True
                line.sendMessage(to, 'Success activated autoadd')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                line.sendMessage(to, 'Autoadd already deactive')
            else:
                settings['autoAdd']['status'] = False
                line.sendMessage(to, 'Success deactivated autoadd')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    line.sendMessage(to, 'Reply message autoadd already active')
                else:
                    settings['autoAdd']['reply'] = True
                    line.sendMessage(to, 'Success activate reply message autoadd')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    line.sendMessage(to, 'Reply message autoadd already deactive')
                else:
                    settings['autoAdd']['reply'] = False
                    line.sendMessage(to, 'Success deactivate reply message autoadd')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoAdd']['message'] = textt
            line.sendMessage(to, 'Success change autoadd message to `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───[ Auto Join ]'
        res += '\n├➢ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├➢ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├➢ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'autojoin':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already active')
            else:
                settings['autoJoin']['status'] = True
                line.sendMessage(to, 'Success activated autojoin')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already deactive')
            else:
                settings['autoJoin']['status'] = False
                line.sendMessage(to, 'Success deactivated autojoin')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already active')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendMessage(to, 'Success activate reply message autojoin')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already deactive')
                else:
                    settings['autoJoin']['reply'] = False
                    line.sendMessage(to, 'Success deactivate reply message autojoin')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'Autojoin ticket already active')
                else:
                    settings['autoJoin']['ticket'] = True
                    line.sendMessage(to, 'Success activate autojoin ticket')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'Autojoin ticket already deactive')
                else:
                    settings['autoJoin']['ticket'] = False
                    line.sendMessage(to, 'Success deactivate autojoin ticket')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoJoin']['message'] = textt
            line.sendMessage(to, 'Success change autojoin message to `%s`' % textt)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───[ Auto Respond ]'
        res += '\n├➢ Status : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├➢ Reply Message : ' + settings['autoRespondMention']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}AutoRespondMention'
        res += '\n│ • {key}AutoRespondMention <on/off>'
        res += '\n│ • {key}AutoRespondMention <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'autorespondmention':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                line.sendMessage(to, 'Autorespondmention already active')
            else:
                settings['autoRespondMention']['status'] = True
                line.sendMessage(to, 'Success activated autorespondmention')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                line.sendMessage(to, 'Autorespondmention already deactive')
            else:
                settings['autoRespondMention']['status'] = False
                line.sendMessage(to, 'Success deactivated autorespondmention')
        else:
            settings['autoRespondMention']['message'] = textt
            line.sendMessage(to, 'Success change autorespondmention message to `%s`' % textt)
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───[ Auto Respond ]'
        res += '\n├➢ Status : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├➢ Reply Message : ' + settings['autoRespond']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}AutoRespond'
        res += '\n│ • {key}AutoRespond <on/off>'
        res += '\n│ • {key}AutoRespond <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'autorespond':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                line.sendMessage(to, 'Autorespond already active')
            else:
                settings['autoRespond']['status'] = True
                line.sendMessage(to, 'Success activated autorespond')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                line.sendMessage(to, 'Autorespond already deactive')
            else:
                settings['autoRespond']['status'] = False
                line.sendMessage(to, 'Success deactivated autorespond')
        else:
            settings['autoRespond']['message'] = textt
            line.sendMessage(to, 'Success change autorespond message to `%s`' % textt)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                line.sendMessage(to, 'Autoread already active')
            else:
                settings['autoRead'] = True
                line.sendMessage(to, 'Success activated autoread')
        elif texttl == 'off':
            if not settings['autoRead']:
                line.sendMessage(to, 'Autoread already deactive')
            else:
                settings['autoRead'] = False
                line.sendMessage(to, 'Success deactivated autoread')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already active')
            else:
                settings['checkContact'] = True
                line.sendMessage(to, 'Success activated checkcontact')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already deactive')
            else:
                settings['checkContact'] = False
                line.sendMessage(to, 'Success deactivated checkcontact')
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                line.sendMessage(to, 'Checkpost already active')
            else:
                settings['checkPost'] = True
                line.sendMessage(to, 'Success activated checkpost')
        elif texttl == 'off':
            if not settings['checkPost']:
                line.sendMessage(to, 'Checkpost already deactive')
            else:
                settings['checkPost'] = False
                line.sendMessage(to, 'Success deactivated checkpost')
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                line.sendMessage(to, 'Checksticker already active')
            else:
                settings['checkSticker'] = True
                line.sendMessage(to, 'Success activated checksticker')
        elif texttl == 'off':
            if not settings['checkSticker']:
                line.sendMessage(to, 'Checksticker already deactive')
            else:
                settings['checkSticker'] = False
                line.sendMessage(to, 'Success deactivated checksticker')
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = '╭───[ My Profile ]'
        res += '\n├➢ MID : ' + profile.mid
        res += '\n├➢ Display Name : ' + str(profile.displayName)
        res += '\n├➢ Status Message : ' + str(profile.statusMessage)
        res += '\n├➢ Usage : '
        res += '\n│ • {key}MyProfile'
        res += '\n│ • {key}MyProfile MID'
        res += '\n│ • {key}MyProfile Name'
        res += '\n│ • {key}MyProfile Bio'
        res += '\n│ • {key}MyProfile Pict'
        res += '\n│ • {key}MyProfile Cover'
        res += '\n│ • {key}MyProfile Change Name <name>'
        res += '\n│ • {key}MyProfile Change Bio <bio>'
        res += '\n│ • {key}MyProfile Change Pict'
        res += '\n│ • {key}MyProfile Change Cover'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'myprofile':
            if profile.pictureStatus:
                line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            line.sendMessage(to, '[ MID ]\n' + str(profile.mid))
        elif texttl == 'name':
            line.sendMessage(to, '[ Display Name ]\n' + str(profile.displayName))
        elif texttl == 'bio':
            line.sendMessage(to, '[ Status Message ]\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '[ Picture Status ]\n' + path)
            else:
                line.sendMessage(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '[ Cover Picture ]\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    line.sendMessage(to, 'Success change display name, changed to `%s`' % name)
                else:
                    line.sendMessage(to, 'Failed change display name, the length of the name cannot be more than 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 500:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    line.sendMessage(to, 'Success change status message, changed to `%s`' % bio)
                else:
                    line.sendMessage(to, 'Failed change status message, the length of the bio cannot be more than 500')
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                line.sendMessage(to, 'Please send the image to set in picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                line.sendMessage(to, 'Please send the image to set in cover profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == "changevp":
	    settings["changevp"] = True
	    line.sendReplyMessage(msg_id, to, "Kirim video nya")
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = '╭───[ My Profile ]'
        if profile:
            res += '\n├➢ MID : ' + profile.mid
            res += '\n├➢ Display Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\n├➢ Status Message : ' + str(profile.statusMessage)
        res += '\n├➢ Usage : '
        res += '\n│ • {key}Profile'
        res += '\n│ • {key}Profile Mid'
        res += '\n│ • {key}Profile Name'
        res += '\n│ • {key}Profile Bio'
        res += '\n│ • {key}Profile Pict'
        res += '\n│ • {key}Profile Cover'
        res += '\n│ • {key}Profile Steal Profile <mention>'
        res += '\n│ • {key}Profile Steal Mid <mention>'
        res += '\n│ • {key}Profile Steal Name <mention>'
        res += '\n│ • {key}Profile Steal Bio <mention>'
        res += '\n│ • {key}Profile Steal Pict <mention>'
        res += '\n│ • {key}Profile Steal Cover <mention>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'profile':
            if profile:
                if profile.pictureStatus:
                    line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL(profile.mid)
                line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '[ MID ]\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '[ Display Name ]\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '[ Status Message ]\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '[ Picture Status ]\n' + path)
            else:
                line.sendMessage(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '[ Cover Picture ]\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        if profile.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───[ Profile ]'
                        res += '\n├➢ MID : ' + profile.mid
                        res += '\n├➢ Display Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\n├➢ Status Message : ' + str(profile.statusMessage)
                        res += '\n╰───[ We Bare Bears Corps™ ]'
                        line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal profile, no one user mentioned')
            elif textsl.startswith('mid '):
                res = '╭───[ MID ]'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return line.sendMessage(to, '[ MID ]\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n│ %i. %s' % (no, mid)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal mid, no one user mentioned')
            elif textsl.startswith('name '):
                res = '╭───[ Display Name ]'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '[ Display Name ]\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.displayName)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal display name, no one user mentioned')
            elif textsl.startswith('bio '):
                res = '╭───[ Status Message ]'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '[ Status Message ]\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.statusMessage)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal status message, no one user mentioned')
            elif textsl.startswith('pict '):
                res = '╭───[ Picture Status ]'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendMessage(to, '[ Picture Status ]\n' + path)
                        else:
                            return line.sendMessage(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n│ %i. %s' % (no, path)
                        else:
                            res += '\n│ %i. Not Found' % no
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal picture status, no one user mentioned')
            elif textsl.startswith('cover '):
                res = '╭───[ Cover Picture ]'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendMessage(to, '[ Cover Picture ]\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n│ %i. %s' % (no, cover)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal cover picture, no one user mentioned')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                try:
                    name = line.getContact(target).displayName
                except TalkException:
                    name = 'Unknown'
                targets += '\n│ %i. %s//%s' % (no, name, bool_dict[status][1])
        else:
            targets += '\n│ Nothing'
        res = '╭───[ Mimic ]'
        res += '\n├➢ Status : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├➢ List :'
        res += targets
        res += '\n├➢ Usage : '
        res += '\n│ • {key}Mimic'
        res += '\n│ • {key}Mimic <on/off>'
        res += '\n│ • {key}Mimic Reset'
        res += '\n│ • {key}Mimic Add <mention>'
        res += '\n│ • {key}Mimic Del <mention>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'mimic':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['mimic']['status']:
                line.sendMessage(to, 'Mimic already active')
            else:
                settings['mimic']['status'] = True
                line.sendMessage(to, 'Success activated mimic')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                line.sendMessage(to, 'Mimic already deactive')
            else:
                settings['mimic']['status'] = False
                line.sendMessage(to, 'Success deactivated mimic')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            line.sendMessage(to, 'Success reset mimic list')
        elif texttl.startswith('add '):
            res = '╭───[ Mimic ]'
            res += '\n├➢ Status : Add Target'
            res += '\n├➢ Added :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───[ We Bare Bears Corps™ ]'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed add mimic target, no one user mentioned')
        elif texttl.startswith('del '):
            res = '╭───[ Mimic ]'
            res += '\n├➢ Status : Del Target'
            res += '\n├➢ Deleted :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───[ We Bare Bears Corps™ ]'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed del mimic target, no one user mentioned')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
      if msg._from in Owner or msg._from in Staff:
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Broadcast 」'
        res += '\n├ Broadcast Type : '
        res += '\n│ 1 : Friends'
        res += '\n│ 2 : Groups'
        res += '\n│ 0 : All'
        res += '\n├ Usage : '
        res += '\n│ • {key}Broadcast'
        res += '\n│ • {key}Broadcast <type> <message>'
        res += '\n╰───「 We Bare Bears Corps™ 」'
        if cmd == 'broadcast':
          if msg._from in Owner or msg._from in Staff:
            line.sendReplyMessage(msg.id, to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
          if msg._from in Owner or msg._from in Staff:
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            bot = line.getAllContactIds()
            migii = 'uc68c1adc2fb449180a296bc50942affd'
            res = '「 Friend Broadcast 」\n'
            res += 'Selfbot by : @! \n'
            res += 'Sender by : @! \n'
            res += 'Send to %i Friends' % len(bot)
            res += '\n__________________________\n\n' 
            res += textt[2:]
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    sendMention(target, res,[migii, sender])
                except TalkException:
                    targets.remove(target)
                    continue
            line.sendReplyMessage(msg.id, to, 'Success broadcast to all friends, sent to %i friends' % len(targets))
        elif cond[0] == '2':
          if msg._from in Owner or msg._from in Staff:
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            bot = line.getGroupIdsJoined()
            migii = 'uc68c1adc2fb449180a296bc50942affd'
            res = '「 Group Broadcast 」\n'
            res += 'Selfbot by : @! \n'
            res += 'Sender by : @! \n'
            res += 'Send to %i Groups' % len(bot)
            res += '\n__________________________\n\n' 
            res += textt[2:]
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    sendMention(target, res,[migii, sender])
                except TalkException:
                    targets.remove(target)
                    continue
            line.sendReplyMessage(msg.id, to, 'Success broadcast to all groups, sent to %i groups' % len(targets))
        elif cond[0] == '0':
          if msg._from in Owner or msg._from in Staff:
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            res = '「 All Broadcast 」\n'
            res += 'Sender by : @! \n\n'
            res += textt[2:]
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    sendMention(target, res,[sender])
                except TalkException:
                    targets.remove(target)
                    continue
            line.sendReplyMessage(msg.id, to, 'Success broadcast to all groups and friends, sent to %i groups and friends' % len(targets))
        else:
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
    elif cmd.startswith("footergbc "):
        bob = text.split(" ")
        hey = text.replace(bob[0] + " ", "")
        text = "「 Broadcast Message 」\n"
        text += "{}".format(hey)
        groups = line.getGroupIdsJoined()
        for gr in groups:
            sendFooter(to,text)
        line.sendReplyMessage(msg.id, to, 'Success broadcast to all groups, sent to %i groups' % len(groups))
    elif cmd.startswith('friendlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───[ Friend List ]'
        res += '\n├➢ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├➢ Usage : '
        res += '\n│ • {key}FriendList'
        res += '\n│ • {key}FriendList Info <num/name>'
        res += '\n│ • {key}FriendList Add <mention>'
        res += '\n│ • {key}FriendList Del <mention/num/name/all>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        ress.append(res)
        if cmd == 'friendlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed display info friend, nothing friend in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───[ Contact Info ]'
                    res += '\n├➢ MID : ' + contact.mid
                    res += '\n├➢ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├➢ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───[ Contact Info ]'
                        res += '\n├➢ MID : ' + contact.mid
                        res += '\n├➢ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├➢ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───[ We Bare Bears Corps™ ]'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───[ Friend List ]'
            res += '\n├➢ Status : Add Friend'
            res += '\n├➢ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───[ We Bare Bears Corps™ ]'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed add contact to friend list, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed del contact from friend list, nothing friend in list')
            res = '╭───[ Friend List ]'
            res += '\n├➢ Status : Del Friend'
            res += '\n├➢ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.deleteContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'Failed del friend with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───[ We Bare Bears Corps™ ]'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───[ Block List ]'
        res += '\n├➢ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├➢ Usage : '
        res += '\n│ • {key}BlockList'
        res += '\n│ • {key}BlockList Info <num/name>'
        res += '\n│ • {key}BlockList Add <mention>'
        res += '\n│ • {key}BlockList Del <mention/num/name/all>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed display info blocked user, nothing user in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───[ Contact Info ]'
                    res += '\n├➢ MID : ' + contact.mid
                    res += '\n├➢ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├➢ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───[ Contact Info ]'
                        res += '\n├➢ MID : ' + contact.mid
                        res += '\n├➢ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├➢ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├➢ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───[ We Bare Bears Corps™ ]'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───[ Block List ]'
            res += '\n├➢ Status : Add Block'
            res += '\n├➢ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───[ We Bare Bears Corps™ ]'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed block contact, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed unblock contact, nothing user in list')
            res = '╭───[ Block List ]'
            res += '\n├➢ Status : Del Block'
            res += '\n├➢ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.unblockContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'Failed unblock user with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───[ We Bare Bears Corps™ ]'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'mentionall':
        members = []
        if msg.toType == 1:
            room = line.getCompactRoom(to)
            members = [mem.mid for mem in room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup(to)
            members = [mem.mid for mem in group.members]
        else:
            return line.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
        if members:
            mentionMembers(to, members)
    elif cmd.startswith(".mentionall "):
        sep = msg.text.split(" ")
        num = msg.text.replace(sep[0] + " ","")
        gids = line.getGroupIdsJoined()
        gid = gids[int(num) - 1]
        G = line.getGroup(gid)
        members = []
        if msg.toType == 1:
            room = line.getCompactRoom(gid)
            members = [mem.mid for mem in room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup(gid)
            members = [mem.mid for mem in group.members]
        else:
            return line.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
        if members:
            mentionMembers2(gid, members)
            line.sendReplyMessage(msg_id, to, 'Success Remote Mentionall\nIn Group: ' +  str(G.name))
    elif cmd == "clear mention":
            del tagme['ROM'][to]
            line.sendMessage(to, "「 Clear Mention 」\nBerhasil menghapus data Mention di group: {}".format(line.getGroup(to).name))
    elif cmd == "check mention":
            if to in tagme['ROM']:
                moneys = {}
                msgas = ''
                for a in tagme['ROM'][to].items():
                    moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya
                sort = sorted(moneys)
                sort.reverse()
                sort = sort[0:]
                msgas = '「 Mention Me 」'
                h = []
                no = 0
                for m in sort:
                    has = ''
                    nol = -1
                    for kucing in moneys[m][0]:
                        nol+=1
                        has+= '\nline://nv/chatMsg?chatId={}&messageId={} \n{}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))
                    h.append(m)
                    no+=1
                    if m == sort[0]:
                        msgas+= '\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                    else:
                        msgas+= '\n\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                sendMention(to, msgas, h)
            else:
                msgas = 'Sorry @!In {} nothink get a mention'.format(line.getGroup(to).name)
                sendMention(to, msgas, [sender])
    elif cmd.startswith(".ginfo "):
        sep = msg.text.split(" ")
        num = msg.text.replace(sep[0] + " ","")
        gids = line.getGroupIdsJoined()
        gid = gids[int(num) - 1]
        group = line.getCompactGroup(gid)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Tidak Ditemukan'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'https://obs.line-scdn.net/' + group.pictureStatus
        res = "╭───「 Remoted Group Info 」"
        res += '\n├ • User: @!'
        res += '\n├ • Group ID : ' + group.id
        res += '\n├ • Group Name : ' + group.name
        res += '\n├ • Group Creator : ' + gcreator
        res += '\n├ • Created Time : ' + created
        res += '\n├ • Member Count : ' + str(len(group.members))
        res += '\n├ • Pending Count : ' + str(pendings)
        res += '\n├ • QR Status : ' + qr
        res += '\n├ • Ticket : ' + ticket
        res += '\n╰───「 We Bare Bears Corps™ 」'
        line.sendReplyImageWithURL(msg_id, to, path)
        if ccreator:
            line.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': ccreator}, contentType=13)
        line.sendReplyMentionV2(msg_id, to, res, [sender])
    elif cmd == 'groupinfo':
        if msg.toType != 2: return line.sendMessage(to, 'Failed display group info, use this command only on group chat')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───[ Group Info ]'
        res += '\n├➢ ID : ' + group.id
        res += '\n├➢ Name : ' + group.name
        res += '\n├➢ Creator : ' + gcreator
        res += '\n├➢ Created Time : ' + created
        res += '\n├➢ Member Count : ' + str(len(group.members))
        res += '\n├➢ Pending Count : ' + str(pendings)
        res += '\n├➢ QR Status : ' + qr
        res += '\n├➢ Ticket : ' + ticket
        res += '\n╰───[ We Bare Bears Corps™ ]'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        sendFooter(to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───[ Group List ]'
        res += '\n├➢ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├➢ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendMessage(to, 'Failed leave group, nothing group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            line.leaveGroup(gid)
                            leaved.append(gid)
                            time.sleep(0.8)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave all group ♪')
                    else:
                        line.sendMessage(to, 'Failed leave group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───[ Invitation List ]'
        res += '\n├➢ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├➢ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendMessage(to, 'Failed accept group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            line.sendMessage(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'Success accept group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed accept group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            line.sendMessage(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'Success accept group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in accepted:
                                continue
                            line.acceptGroupInvitation(gid)
                            accepted.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'Success accept all invitation group ♪')
                    else:
                        line.sendMessage(to, 'Failed accept group with name `%s`, name not in list ♪' % name)
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return line.sendMessage(to, 'Failed reject group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            line.sendMessage(to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'Success reject group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed reject group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            line.sendMessage(to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'Success reject group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in rejected:
                                continue
                            line.rejectGroupInvitation(gid)
                            rejected.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'Success reject all invitation group ♪')
                    else:
                        line.sendMessage(to, 'Failed reject group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return line.sendMessage(to, 'Failed display member list, use this command only on room or group chat')
        if not members:
            return line.sendMessage(to, 'Failed display member list, no one contact')
        res = '╭───[ Member List ]'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───[ We Bare Bears Corps™ ]'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return line.sendMessage(to, 'Failed display pending list, use this command only on group chat')
        group = line.getGroup(to)
        members = group.invitee
        if not members:
            return line.sendMessage(to, 'Failed display pending list, no one contact')
        res = '╭───[ Pending List ]'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───[ We Bare Bears Corps™ ]'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd.startswith('.infomem '):
                                    separate = msg.text.split(" ")
                                    number = msg.text.replace(separate[0] + " ","")
                                    groups = line.getGroupIdsJoined()
                                    ret_ = ""
                                    try:
                                        group = groups[int(number)-1]
                                        G = line.getGroup(group)
                                        no = 0
                                        ret_ = ""
                                        for mem in G.members:
                                           no += 1
                                           ret_ += "\n " " "+ str(no) + ". " + mem.displayName
                                        line.sendReplyMessage(msg.id, to," Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                                    except:
                                           pass
    elif cmd.startswith(".openqr "):
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    groups = line.getGroupIdsJoined()
                                    group = groups[int(number)-1]
                                    G = line.getGroup(group)
                                    G.preventedJoinByTicket = False
                                    line.updateGroup(G)
                                    url = line.reissueGroupTicket(group)
                                    ticket = 'Sukses Remoted Commands\nOpen qr in groups {}\nlink: https://line.me/R/ti/g/{}'.format(G.name,url)
                                    sendFooter(to,ticket)
    elif cmd.startswith(".closeqr "):
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    groups = line.getGroupIdsJoined()
                                    group = groups[int(number)-1]
                                    G = line.getGroup(group)
                                    G.preventedJoinByTicket = True
                                    line.updateGroup(G)
                                    ticket = 'Sukses Remoted Commands\nClose qr in groups {}'.format(G.name)
                                    sendFooter(to,ticket)
    elif cmd == 'openqr':
        if msg.toType != 2: return line.sendMessage(to, 'Failed open qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        sendFooter(to, 'Success open group qr, you must be careful')
    elif cmd == 'closeqr':
        if msg.toType != 2: return line.sendMessage(to, 'Failed close qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        sendFooter(to, 'Success close group qr')
    elif cmd.startswith('changegroupname '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed change group name, use this command only on group chat')
        group = line.getCompactGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return line.sendMessage(to, 'Failed change group name, the number of names cannot exceed 50')
        group.name = gname
        line.updateGroup(group)
        line.sendMessage(to, 'Success change group name to `%s`' % gname)
    elif cmd == 'changegrouppict':
        if msg.toType != 2: return line.sendMessage(to, 'Failed change group picture, use this command only on group chat')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            line.sendMessage(to, 'Please send the image, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
        else:
            line.sendMessage(to, 'Command already active, please send the image or type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
    elif cmd == 'kickall':
        if msg.toType != 2: return line.sendMessage(to, 'Failed kick all members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.members:
            return line.sendMessage(to, 'Failed kick all members, no member in list')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except:pass
    elif cmd == 'cancelall':
        if msg.toType != 2: return line.sendMessage(to, 'Failed cancel all pending members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.invitee:
            return line.sendMessage(to, 'Failed cancel all pending members, no pending member in list')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except:pass
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = '╭───[ Lurking ]'
        if msg.toType in [1, 2]: res += '\n├➢ Status : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\n├➢ Reply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\n├➢ Reply Reader Message : ' + lurking[to]['reply']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}Lurk'
        res += '\n│ • {key}Lurk <on/off>'
        res += '\n│ • {key}Lurk Result'
        res += '\n│ • {key}Lurk Reset'
        res += '\n│ • {key}Lurk ReplyReader <on/off>'
        res += '\n│ • {key}Lurk ReplyReader <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'lurk':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return line.sendMessage(to, 'Failed execute command lurking, use this command only on room or group chat')
        elif texttl == 'on':
            if lurking[to]['status']:
                line.sendMessage(to, 'Lurking already active')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'Success activated lurking')
        elif texttl == 'off':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Lurking already deactive')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                line.sendMessage(to, 'Success deactivated lurking')
        elif texttl == 'result':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Failed display lurking result, lurking has not been activated')
            else:
                if not lurking[to]['members']:
                    line.sendMessage(to, 'Failed display lurking result, no one members reading')
                else:
                    members = lurking[to]['members']
                    res = '╭───[ Lurking ]'
                    if msg.toType == 2: res += '\n├➢ Group Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n│'
                                res += '\n├➢ Time Set : ' + lurking[to]['time']
                                res += '\n╰───[ We Bare Bears Corps™ ]'
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMessage(to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Failed reset lurking, lurking has not been activated')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'Success resetted lurking')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    line.sendMessage(to, 'Reply reader already active')
                else:
                    lurking[to]['reply']['status'] = True
                    line.sendMessage(to, 'Success activated reply reader')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    line.sendMessage(to, 'Reply reader already deactive')
                else:
                    lurking[to]['reply']['status'] = False
                    line.sendMessage(to, 'Success deactivated reply reader')
            else:
                lurking[to]['reply']['message'] = texts
                line.sendMessage(to, 'Success set reply reader message to `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───[ Greet Message ]'
        res += '\n├➢ Greetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├➢ Greetings Join Message : ' + settings['greet']['join']['message']
        res += '\n├➢ Greetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├➢ Greetings Join Message : ' + settings['greet']['leave']['message']
        res += '\n├➢ Usage : '
        res += '\n│ • {key}Greet'
        res += '\n│ • {key}Greet Join <on/off>'
        res += '\n│ • {key}Greet Join <message>'
        res += '\n│ • {key}Greet Leave <on/off>'
        res += '\n│ • {key}Greet Leave <message>'
        res += '\n╰───[ We Bare Bears Corps™ ]'
        if cmd == 'greet':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendMessage(to, 'Greetings join already active')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendMessage(to, 'Success activated greetings join')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendMessage(to, 'Greetings join already deactive')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendMessage(to, 'Success deactivated greetings join')
            else:
                settings['greet']['join']['message'] = texts
                line.sendMessage(to, 'Success change greetings join message to `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendMessage(to, 'Greetings leave already active')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendMessage(to, 'Success activated greetings leave')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendMessage(to, 'Greetings leave already deactive')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendMessage(to, 'Success deactivated greetings leave')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendMessage(to, 'Success change greetings leave message to `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invite '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed invite member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                except:pass
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                except:pass
    elif cmd.startswith('vkick'):
        if msg.toType != 2: return line.sendMessage(to, 'Failed vultra kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                    line.inviteIntoGroup(to, [mid])
                except:pass
    elif cmd.startswith('reinvite '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                except:pass
    elif cmd.startswith('mkick '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed multi kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                    line.inviteIntoGroup(to, [mid])
                except:pass
    elif cmd == 'xkick':
                if msg.relatedMessageId is not None:
                    aa = line.getRecentMessagesV2(to, 1001)
                    for bb in aa:
                        if bb.id in msg.relatedMessageId:
                            line.kickoutFromGroup(to, [bb._from])
                            break
                else:
                    line.sendMessage(to, 'you must reply the message')
    elif cmd == 'xinvite':
                if msg.relatedMessageId is not None:
                    aa = line.getRecentMessagesV2(to, 1001)
                    for bb in aa:
                        if bb.id in msg.relatedMessageId:
                            line.findAndAddContactsByMid(bb._from)
                            line.inviteIntoGroup(to, [bb._from])
                            break
                else:
                    line.sendMessage(to, 'you must reply the message')
    elif cmd == "purge":
                            if msg.toType == 2:
                                group = line.getGroup(to)
                                nama = [contact.mid for contact in group.members]
                                lists = []
                                for tag in ban["blacklist"]:
                                    lists+=filter(lambda str: str == tag, nama)
                                if lists == []:
                                    line.sendReplyMessage(msg.id,to, "Blacklist not detected!")
                                    return
                                for jj in lists:
                                    line.kickoutFromGroup(to,[jj])
                                line.sendReplyMessage(msg.id, to,"Blacklist has been purge")
#================Feature================
    elif cmd.startswith("unsend "):
        sep = msg.text.split(" ")
        args = msg.text.replace(sep[0] + " ","")
        mes = int(sep[1])
        M = line.getRecentMessagesV2(to, 1001)
        MId = []
        for ind,i in enumerate(M):
            if ind == 0:
                pass
            else:
                if i._from == line.profile.mid:
                    MId.append(i.id)
                    if len(MId) == mes:
                        break
        def unsMes(id):
            line.unsendMessage(id)
        for i in MId:
            thread1 = threading.Thread(target=unsMes, args=(i,))
            thread1.daemon = True
            thread1.start()
            thread1.join()
        line.unsendMessage(msg.id)
    elif cmd.startswith('.unsend '):
        sep = text.split(" ")
        num = int(sep[1])
        numb = int(sep[2])
        sep2 = text.replace(sep[0] + ' ','')
        text = sep2.replace(sep[1] + ' ','')
        groups = line.getGroupIdsJoined()
        group = groups[int(num) - 1]
        G = line.getGroup(group)
        M = line.getRecentMessagesV2(group, 1001)
        MId = []
        for ind,i in enumerate(M):
            if ind == 0:
                pass
            else: 
                if i._from == line.profile.mid:
                    MId.append(i.id)
                    if len(MId) == numb:
                        break
        def unsMes(id):
            line.unsendMessage(id)
        for i in MId:
            thread1 = threading.Thread(target=unsMes, args=(i,))
            thread1.daemon = True
            thread1.start()
            thread1.join()
        line.unsendMessage(msg.id)
        res = 'Sukses Remoted Commands'
        res += '\nTotal unsend {} message.'.format(len(MId))
        res += '\nIn Group :' + G.name
        line.sendReplyMessage(msg.id, to, res)
    elif cmd.startswith('unsend '):
      if msg._from in Owner:
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        G = line.getGroup(to)
        if texttl == 'on':
            if settings["unsendMessage"]:
                line.sendReplyMessage(msg.id, to, 'Unsend already active')
            else:
                settings["unsendMessage"] = True
                line.sendReplyMessage(msg.id, to, '「 Notifikasi 」\nDetect unsend berhasil diaktifkan\nDi Group ' +  str(G.name))
        elif texttl == 'off':
            if not settings["unsendMessage"]:
                line.sendReplyMessage(msg.id, to, 'Unsend already deactive')
            else:
                settings["unsendMessage"] = False
                line.sendReplyMessage(msg.id, to, '「 Notifikasi 」\nDetect unsend berhasil dimatikan\nDi Group ' +  str(G.name))
    elif cmd.startswith("lastseen ") and msg.toType == 2:
            if 'MENTION' in msg.contentMetadata.keys() != None:
                names = re.findall(r'@(\w+)', msg.text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                    if mention['M'] in lastseen["find"]:
                        line.sendMentionV2(to, "@!{}".format(lastseen["username"][mention['M']]), [mention['M']])
                    else:
                        line.sendMentionV2(to, "Oops!!\nI can't found @!",[mention['M']])
    elif cmd.startswith("find "):
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                profile = line.getContact(mention['M'])
                aa = line.getGroupIdsJoined()
                target = profile.mid
                lacak = "";num = 1
                for x in aa:
                    member = [c.mid for c in line.getGroup(x).members]
                    if target in member:
                        lacak += "\n{}. {}".format(num,line.getGroup(x).name)
                        num = (num+1)
                if lacak == "":line.sendReplyMessage(msg_id, to,"not found")
                else:
                    pesan = "  [  Locate  ]\nUser : {}\nGroup Joined:{}".format(line.getContact(target).displayName, lacak)
                    line.sendReplyMessage(msg_id, to, pesan)
    elif cmd.startswith("spamtag "):
            dan = text.split(" ")
            num = int(dan[1])
            text = "「 Spamtag 」\nBerhasil {} Spamtag".format(str(dan[1]))
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                lists = []
                for mention in mentionees:
                    if mention["M"] not in lists:
                        lists.append(mention["M"])
                for ls in lists:
                    for var in range(0,num):
                        sendMention(to, "@!", [ls])
                line.sendMessage(to, text)
    elif cmd.startswith("spamcallto "):
            dan = text.split(" ")
            num = int(dan[1])
            ret_ = "╭───[ Spamcall Mention ]"
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                lists = []
                for mention in mentionees:
                    if mention["M"] not in lists:
                        lists.append(mention["M"])
                for ls in lists:
                    for var in range(0,num):
                        group = line.getGroup(to)
                        members = [ls]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    ret_ += "\n├➢ @!"
                ret_ += "\n╰───[ Total {} Spam call]".format(str(dan[1]))
                sendMention(to, ret_, lists)
    elif cmd.startswith('.spamcall '):
        sep = text.split(" ")
        num = int(sep[1])
        numb = int(sep[2])
        sep2 = text.replace(sep[0] + ' ','')
        text = sep2.replace(sep[1] + ' ','')
        groups = line.getGroupIdsJoined()
        group = groups[int(num) - 1]
        G = line.getGroup(group)
        line.sendMessage(to, "Succesfully Spam Call to Group: " + G.name)
        for var in range(0,numb):
            G = line.getGroup(group)
            members = [mem.mid for mem in G.members]
            line.acquireGroupCallRoute(group)
            line.inviteIntoGroupCall(group, contactIds=members)
    elif cmd.startswith("spamtext "):
            spam = text.split(" ")
            for asw in range(int(spam[1])):
                line.sendReplyMessage(msg.id, to, str(text.replace(spam[0] + " " + spam[1] + " ","")))
    elif cmd == 'sider off':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    wait["Sider"] = False
                                    G = line.getGroup(to)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    res = '「 Sider Off 」'
                                    res += '\nSider berhasil Dimatikan'
                                    res += '\nDi Group : ' +  str(G.name)
                                    res += '\nTanggal :'  + datetime.strftime(timeNow,'%d-%m-%Y')
                                    res += '\nJam : ' +  datetime.strftime(timeNow,'%H:%M:%S')
                                    line.sendReplyMessage(msg.id, to, res)
                                else:
                                    line.sendReplyMessage(msg.id, msg.to, '「 Sider Off 」\n Sudah Tidak Aktif')
    elif cmd == 'sider on':
                                try:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    G = line.getGroup(msg.to)
                                    timeNow = datetime.now(tz=tz)
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                           pass
                                           cctv['point'][msg.to] = msg.id
                                           cctv['sidermem'][msg.to] = ""
                                           cctv['cyduk'][msg.to]=True
                                           wait["Sider"] = True
                                           res = '「 Sider On 」'
                                           res += '\nSider berhasil Diaktifkan'
                                           res += '\nDi Group : ' + str(G.name)
                                           res += '\nTanggal : ' + datetime.strftime(timeNow,'%d-%m-%Y')
                                           res += '\nJam : ' +  datetime.strftime(timeNow,'%H:%M:%S')
                                           line.sendReplyMessage(msg.id, to, res)
def executeOp(op):
    try:
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 11 or op.type == 122:
            if op.param1 in settings["protectqr"]:
                try:
                    if line.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in settings["whitelist"]:
                            ban["blacklist"].append(op.param2)
                            line.reissueGroupTicket(op.param1)
                            X = line.getCompactGroup(op.param1)
                            X.preventedJoinByTicket = True
                            line.updateGroup(X)
                            line.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
        if op.type == 13 or op.type == 124:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
            if op.param3 in ban["blacklist"]:
                if op.param2 not in settings["whitelist"]:
                    try:
                        anu = line.getCompactGroup(op.param1)
                        if anu.invitee is not None:
                            pipo = [a.mid for a in anu.invitee]
                            for target in pipo:
                                if target in op.param3:
                                    try:
                                        line.cancelGroupInvitation(op.param1,[target])
                                        line.kickoutFromGroup(op.param1,[op.param2])
                                        line.sendMessage(op.param1, "Don't invite someone on my blacklist")
                                    except:
                                        pass
                    except:pass
                else:pass
                if op.param2 not in ban["blacklist"]:
                    if op.param2 not in settings["whitelist"]:
                        wait['blacklist'].append(op.param2)
                    else:pass
                else:pass
            if op.param1 in settings["protectinvite"]:
                if op.param2 not in settings["whitelist"]:
                    try:
                        if op.param2 not in ban['blacklist']:
                            ban['blacklist'].append(op.param2)
                        else:pass
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])                                         
                        except:pass
                        mbul = line.getGroup(op.param1)
                        no = 0
                        for a in mbul.invitee:
                            if a.mid in op.param3:
                                if no > 10:pass
                                else:
                                    try:
                                        no = (no+1)
                                        line.cancelGroupInvitation(op.param1,[a.mid])
                                        time.sleep(0.04)
                                    except:pass
                        for b in mbul.members:
                            if b.mid in op.param3:
                                try:
                                    line.kickoutFromGroup(op.param1,[b.mid])
                                except:pass
                    except:pass
                else:pass
        if op.type == 15 or op.type == 128:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 17 or op.type == 130:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
            if op.param2 in ban["blacklist"]:
                try:
                    group = line.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    line.updateGroup(group)
                    line.kickoutFromGroup(op.param1,[op.param2])
                    group.preventedJoinByTicket = True
                    line.updateGroup(group)
                except Exception as e:
                    group = line.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    line.kickoutFromGroup(op.param1,[op.param2])
                    line.updateGroup(group)
            if op.param2 in ban["blacklist"]:
                try:
                    line.kickoutFromGroup(op.param1,[op.param2])
                except:pass
            if op.param1 in settings["protectjoin"]:
                if op.param2 not in settings["whitelist"]:
                    ban["blacklist"].append(op.param2)
                    try:
                        if op.param3 not in ban["blacklist"]:
                        	line.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
        if op.type == 19 or op.type == 133:
          if op.param3 in myMid:
                ban["blacklist"].append(op.param2)
                group = "Mid GC" #mid gc dapat di lihat di groupinfo
                nameGroup = line.getGroup(op.param1).name
                jam = pytz.timezone("Asia/Jakarta")
                jamSek = datetime.now(tz=jam)
                jamm = datetime.strftime(jamSek, '%d-%m-%Y')
                jammm = datetime.strftime(jamSek,'%H:%M:%S')
                contact = line.getContact(myMid)
                kiker = line.getContact(op.param2)
                res = "╭───[ Notifikasi Kick ]"
                res += "\n├➢ In Group: {}".format(nameGroup)
                res += "\n├➢ Date: {}".format(jamm)
                res += "\n├➢ Time: {}".format(jammm)
                res += "\n├➢ Victim : {}".format(contact.displayName)
                res += "\n├➢ Kicker: {}".format(kiker.displayName)
                res += "\n├ 👇Contact Kicker👇"
                res += "\n╰───[ We Bare Bears Corps™ ]"
                data = {
                                           "type": "text",
                                           "text": "{}".format(str(res)),
                                           "sentBy": {
                                           "label": "{}".format(line.getContact(myMid).displayName),
                                           "iconUrl": "https://obs.line-scdn.net/{}".format(line.getContact(myMid).pictureStatus),
                                           "linkUrl": "https://line.me/ti/p/~imbobby_",
                                         }
                                     }
                sendTemplate(group, data)
                line.sendContact(group, op.param2)
          if op.param3 in settings["whitelist"]:
                if op.param2 not in settings["whitelist"]:
                    try:
                        line.findAndAddContactsByMid(op.param3)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        line.sendMessage(op.param1,"Don't Kick My Whitelist !!")
                    except:pass
          if op.param1 in settings["protectkick"]:
                if op.param2 not in settings["whitelist"]:
                    ban["blacklist"].append(op.param2)
                    line.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32 or op.type == 126:
          if op.param3 in settings["whitelist"]:
                if op.param2 not in settings["whitelist"]:
                    try:
                        line.findAndAddContactsByMid(op.param3)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        line.sendMessage(op.param1,"Don't Cancel My Whitelist !!")
                    except:pass
          if op.param1 in settings["protectcancel"]:
                if op.param2 not in settings["whitelist"]:
                    ban["blacklist"].append(op.param2)
                    line.kickoutFromGroup(op.param1,[op.param2])
                else:pass
        if op.type == 25:
            print ("++ Operation : ( 25 ) SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == 'clearchat':
                    line.removeAllMessages(op.param2)
                    sendFooter(to, "Allchat deleted")
                elif text.lower() == 'autolike on':
                    settings["autolike"] = True
                    sendFooter(to, "Auto like actived")
                elif text.lower() == 'autolike off':
                    settings["autolike"] = False
                    sendFooter(to, "Auto like non actived")
                elif text.lower() == 'autocomment on':
                    settings["autokomen"] = True
                    sendFooter(to, "Auto comment actived")
                elif text.lower() == 'autocomment off':
                    settings["autokomen"] = False
                    sendFooter(to, "Auto comment non actived")
                elif msg.text.lower().startswith("allmid"):
                                if msg.toType == 2:
                                    group = line.getGroup(to)
                                    num = 0
                                    ret_ = "╭───[ Mid List On Group {} ]".format(group.name)
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n├➢ {}.{}\n├➢ {}".format(num, contact.displayName, contact.mid)
                                    ret_ += "\n╰───[ Total {} Members ]".format(len(group.members))
                                    line.sendReplyMessage(msg_id, to, ret_)
                elif msg.text.lower().startswith("spamcall "):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    line.sendMessage(to, "Succesfully Spam Call to Group")
                                    for var in range(0,num):
                                       group = line.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       line.acquireGroupCallRoute(to)
                                       line.inviteIntoGroupCall(to, contactIds=members)
                elif msg.text.lower().startswith("gift"):
                                line.generateReplyMessage(msg.id)
                                line.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                                line.sendMessage(to, "for you")
                elif msg.text.lower().startswith("ytmp4 "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    arifistifik = "╭───[SEARCHING]"
                                    title = "\n├➢ Judul: " + vid.title + ""
                                    author = '\n├➢ Author : ' + str(vid.author)
                                    durasi = '\n├➢ Duration : ' + str(vid.duration)
                                    suka = '\n├➢ Likes : ' + str(vid.likes)
                                    rating = '\n├➢ Rating : ' + str(vid.rating)
                                    dpk = '\n╰───[ We Bare Bears Corps™ ]'
                                line.sendVideoWithURL(msg.to, me)
                                line.sendMessage(msg.to,arifistifik+ title+ author+ durasi+ suka+ rating+ dpk)
                            except Exception as e:
                                line.sendMessage(msg.to,str(e))
                elif msg.text.lower().startswith("ytmp3 "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    arifistifik = "╭───[SEARCHING]"
                                    title = "\n├➢ Judul: " + vid.title + ""
                                    author = '\n├➢ Author : ' + str(vid.author)
                                    durasi = '\n├➢ Duration : ' + str(vid.duration)
                                    suka = '\n├➢ Likes : ' + str(vid.likes)
                                    rating = '\n├➢ Rating : ' + str(vid.rating)
                                    dpk = '\n╰───[ We Bare Bears Corps™ ]'
                                line.sendAudioWithURL(msg.to, me)
                                line.sendMessage(msg.to,arifistifik+ title+ author+ durasi+ suka+ rating+ dpk)
                            except Exception as e:
                                line.sendMessage(msg.to,str(e))
                elif msg.text.lower().startswith("instagram "):
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['graphql']['user']['full_name'])
                                bioIG = str(data['graphql']['user']['biography'])
                                mediaIG = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                                verifIG = str(data['graphql']['user']['is_verified'])
                                usernameIG = str(data['graphql']['user']['username'])
                                followerIG = str(data['graphql']['user']['edge_followed_by']['count'])
                                profileIG = data['graphql']['user']['profile_pic_url_hd']
                                privateIG = str(data['graphql']['user']['is_private'])
                                followIG = str(data['graphql']['user']['edge_follow']['count'])
                                link = "• Link : " + "https://www.instagram.com/" + instagram
                                text = "「 Instagram User 」\n• Name : "+namaIG+"\n• Username : "+usernameIG+"\n• Follower : "+followerIG+"\n• Following : "+followIG+"\n• Total post : "+mediaIG+"\n• Verified : "+verifIG+"\n• Private : "+privateIG+"\n• Biography : "+bioIG+"" "\n" + link
                                line.sendImageWithURL(msg.to, profileIG)
                                line.sendMessage(msg.to, str(text))
        if op.type == 25 or op.type == 26:
            print ("++ Operation : ( [25:26]) AUTOLIKE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if msg.contentType == 16:
            	if msg.toType in (2,1,0):
                    if settings['autokomen']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                            if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                                contact = line.getContact(sender)
                                author = contact.displayName
                            else:
                                author = msg.contentMetadata['serviceName']
                            posturl = msg.contentMetadata['postEndUrl']
                            rep = posturl.replace("line://home/post?userMid=","")
                            sep = rep.split("&postId=")
                            textt = "Like dengan terpaksa"
                            line.createComment(sender, sep[1], textt)
                    if settings['autolike']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                            if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                                contact = line.getContact(sender)
                                author = contact.displayName
                            else:
                                author = msg.contentMetadata['serviceName']
                            posturl = msg.contentMetadata['postEndUrl']
                            line.sendMessage(to, 'Done Like By Me')
                            rep = posturl.replace("line://home/post?userMid=","")
                            sep = rep.split("&postId=")
                            line.likePost(sender, sep[1], 1001)
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0:
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m already on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, 'Execute command error, ' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, 'Execute command error, ' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendMessage(to, 'Success change picture profile')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendMessage(to, 'Success change cover profile')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.sendMessage(to, 'Success change group picture')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 2: #content type video
                if settings["changevp"] == True:
                    contact = line.getProfile()
                    pict = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                    path = line.downloadFileURL(pict)
                    path1 = line.downloadObjectMsg(msg_id)
                    settings["changevp"] = False
                    changevideopp(path, path1)
                    line.sendMessage(to, "Success change Video Profile")
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───[ Sticker Info ]'
                    res += '\n├➢ Sticker ID : ' + msg.contentMetadata['STKID']
                    res += '\n├➢ Sticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├➢ Sticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\n├➢ Sticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendMessage(to, 'Failed get details contact with mid ' + mid)
                    res = '╭───[ Details Contact ]'
                    res += '\n├➢ MID : ' + mid
                    res += '\n├➢ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├➢ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───[ We Bare Bears Corps™ ]'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendMessage(to, parsingRes(res))
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in ban["blacklist"]:
                        line.sendReplyMessage(msg.id, to,"「 Blacklist 」\nContact Already In Blacklist -_-")
                        wait["wblacklist"] = False
                    else:
                        ban["blacklist"].append(msg.contentMetadata["mid"])
                        line.sendReplyMessage(msg.id, to,"「 Blacklist 」\nSuccess Add Contact To Blacklist ^_^")
                        wait["wblacklist"] = False
                if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in ban["blacklist"]:
                        ban["blacklist"].remove(msg.contentMetadata["mid"])
                        line.sendReplyMessage(msg.id, to,"「 Blacklist 」\nSuccess Delete Contact From Blacklist ^_^")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        line.sendReplyMessage(msg.id, to,"「 Blacklist 」\nContact Not In Blacklist -_-")
                if wait["wwhitelist"] == True:
                    if msg.contentMetadata["mid"] in settings["whitelist"]:
                        line.sendReplyMessage(msg.id, to,"「 Whitelist 」\nContact Already In Whitelist -_-")
                        wait["wwhitelist"] = False
                    else:
                        settings["whitelist"].append(msg.contentMetadata["mid"])
                        line.sendReplyMessage(msg.id, to,"「 Whitelist 」\nSuccess Add Contact To Whitelist ^_^")
                        wait["wwhitelist"] = False
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───[ Details Post ]'
                        res += '\n├➢ Creator : ' + author
                        res += '\n├➢ Post Link : ' + posturl
                        res += '\n╰───[ We Bare Bears Corps™ ]'
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)
            if msg.contentType == 0:
                if msg.toType != 0 and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if myMid in mention["M"]:
                                if line.getProfile().mid in mention["M"]:
                                    if to not in tagme['ROM']:
                                        tagme['ROM'][to] = {}
                                    if sender not in tagme['ROM'][to]:
                                        tagme['ROM'][to][sender] = {}
                                    if 'msg.id' not in tagme['ROM'][to][sender]:
                                        tagme['ROM'][to][sender]['msg.id'] = []
                                    if 'waktu' not in tagme['ROM'][to][sender]:
                                        tagme['ROM'][to][sender]['waktu'] = []
                                    tagme['ROM'][to][sender]['msg.id'].append(msg.id)
                                    tagme['ROM'][to][sender]['waktu'].append(msg.createdTime)
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if msg._from not in myMid:
                            if settings["mentionkick"] == True:
                                name = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    if myMid in mention["M"]:
                                        if line.getProfile().mid in mention["M"]:
                                            sendMention(to,"Ngetag sih, jadi kena kick kan @!", [msg._from])
                                            line.kickoutFromGroup(msg.to, [msg._from])
                                            break
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m already on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])
            try:
                Name = line.getContact(msg._from).mid
                group = line.getGroup(msg.to).name
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = timeNow.strftime('%H.%M')
                readTime2 = hr
                readTime3 = timeNow.strftime('%d') + "-" + bln + "-" + timeNow.strftime('%Y')
                lastseen["username"][Name] = "was lastseen\nin group ' " + group + " '\nat time " + readTime + " WIB\non " + readTime2 + ", " + readTime3
                lastseen['find'][msg._from] = True
            except:
                pass
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
            try:
                Name = line.getContact(op.param2).mid
                group = line.getGroup(op.param1).name
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = timeNow.strftime('%H.%M')
                readTime2 = hr
                readTime3 = timeNow.strftime('%d') + "-" + bln + "-" + timeNow.strftime('%Y')
                lastseen["username"][Name] = "was lastseen\nin group ' " + group + " '\nat time " + readTime + " WIB\non " + readTime2 + ", " + readTime3
                lastseen['find'][op.param2] = True
            except:
                pass
            if op.param1 in readers:
                if readers[op.param1]['status'] and op.param2 not in readers[op.param1]['members']:
                    readers[op.param1]['members'].append(op.param2)
                    if readers[op.param1]['status']:
                        if settings['status']:
                            return
                        if '@!' not in readers[op.param1]['message']:
                            line.sendFakeMessage(op.param1, readers[op.param1]['message'], op.param2)
                            line.sendFakeContact(op.param1, op.param2)
                        else:
                            line.sendMentionV2(op.param1, readers[op.param1]['message'], [op.param2])
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        pelaku = op.param2
                        kontak = line.getContact(op.param2)
                        text = settings["defaultReplyReader"]
                        Name = line.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                                cctv['sidermem'][op.param1] += "\n> " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        line.sendMessageMusic(op.param1, kontak.displayName, 'betah banget jadi sider 😑', 'line.me/ti/p/~imbobby_', "https://obs.line-apps.com/os/p/{}".format(str(kontak.mid)))
                                        #sendMention(op.param1, "Kak @! jelek, sider mulu",[op.param2])
                                        #line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + line.getContact(op.param2).picturePath)
                                    else:
                                        line.sendMessageMusic(op.param1, kontak.displayName, 'sider mulu jomblo ya (｡-_-｡)', 'line.me/ti/p/~imbobby_', "https://obs.line-apps.com/os/p/{}".format(str(kontak.mid)))
                                        #sendMention(op.param1, "Kak @! sider mulu, jomblo ya ka?",[op.param2])
                                        #line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + line.getContact(op.param2).picturePath)
                                else:
                                    line.sendMessageMusic(op.param1, kontak.displayName, 'cie ketahuan sider ( ͡° ͜ʖ ͡°)', 'line.me/ti/p/~imbobby_', "https://obs.line-apps.com/os/p/{}".format(str(kontak.mid)))
                                    #sendMention(op.param1, "Kak @! Jangan Sider dong",[op.param2])
                                    #line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + line.getContact(op.param2).picturePath)
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 65:
            if settings["unsendMessage"]:
                trop = op.param1
                msg_id = op.param2
                if msg_id in bool_dict:
                    if "text" in bool_dict[msg_id]:
                        trops = line.getContact(bool_dict[msg_id]["from"])
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        tro_ = "# Unsend Message"
                        tro_ += "\nSender : {}".format(str(trops.displayName))
                        tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                        tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                        tro_ += "\nType : Text"
                        tro_ += "\nText : {}".format(bool_dict[msg_id]["text"])
                        line.sendReplyMessage(msg_id, trop, str(tro_))
                        del bool_dict[msg_id]
                    else:
                        if "image" in bool_dict[msg_id]:
                            trops = line.getContact(bool_dict[msg_id]["from"])
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            tro_ = "# Unsend Message"
                            tro_ += "\nSender : {}".format(str(trops.displayName))
                            tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                            tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                            tro_ += "\nType : Image"
                            line.sendReplyMessage(msg_id, trop, str(tro_))
                            line.sendImage(trop, bool_dict[msg_id]["image"])
                            del bool_dict[msg_id]
                        else:
                            if "video" in bool_dict[msg_id]:
                                trops = line.getContact(bool_dict[msg_id]["from"])
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                tro_ = "# Unsend Message"
                                tro_ += "\nSender : {}".format(str(trops.displayName))
                                tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                tro_ += "\nType : Video"
                                line.sendReplyMessage(msg_id, trop, str(tro_))
                                line.sendVideo(trop, bool_dict[msg_id]["video"])
                                del bool_dict[msg_id]
                            else:
                                if "audio" in bool_dict[msg_id]:
                                        trops = line.getContact(bool_dict[msg_id]["from"])
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        tro_ = "# Unsend Message"
                                        tro_ += "\nSender : {}".format(str(trops.displayName))
                                        tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                        tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                        tro_ += "\nType : Audio"
                                        line.sendReplyMessage(msg_id, trop, str(tro_))
                                        line.sendAudio(trop, bool_dict[msg_id]["audio"])
                                        del bool_dict[msg_id]
                                else:
                                    if "sticker" in bool_dict[msg_id]:
                                            trops = line.getContact(bool_dict[msg_id]["from"])
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            tro_ = "# Unsend Message"
                                            tro_ += "\nSender : {}".format(str(trops.displayName))
                                            tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                            tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                            tro_ += "\nType : Sticker"
                                            line.sendReplyMessage(msg_id, trop, str(tro_))
                                            line.sendImageWithURL(trop, bool_dict[msg_id]["sticker"])
                                            del bool_dict[msg_id]
                                    else:
                                        if "mid" in bool_dict[msg_id]:
                                                trops = line.getContact(bool_dict[msg_id]["from"])
                                                tro_ = "# Unsend Message"
                                                tro_ += "\nSender : {}".format(str(trops.displayName))
                                                tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                                tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                                tro_ += "\nType : Contact"
                                                line.sendReplyMessage(msg_id, trop, str(tro_))
                                                line.sendContact(trop, bool_dict[msg_id]["mid"])
                                                del bool_dict[msg_id]
                                        else:
                                            if "location" in bool_dict[msg_id]:
                                                    trops = line.getContact(bool_dict[msg_id]["from"])
                                                    tro_ = "# Unsend Message"
                                                    tro_ += "\nSender : {}".format(str(trops.displayName))
                                                    #tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                                    #tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                                    tro_ += "\nType : Location"
                                                    line.sendReplyMessage(msg_id, trop, str(tro_))
                                                    line.sendLocation(trop, bool_dict[msg_id]["location"])
                                                    del bool_dict[msg_id]
                                            else:
                                                if "file" in bool_dict[msg_id]:
                                                        trops = line.getContact(bool_dict[msg_id]["from"])
                                                        tro_ = "# Unsend Message"
                                                        tro_ += "\nSender : {}".format(str(trops.displayName))
                                                        tro_ += "\nTanggal : {}".format(str(datetime.strftime(timeNow,'%d-%m-%Y')))
                                                        tro_ += "\nJam : {}".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                                        tro_ += "\nType : File"
                                                        line.sendReplyMessage(msg_id, trop, str(tro_))
                                                        line.sendFile(trop, bool_dict[msg_id]["file"])
                                                        del bool_dict[msg_id]
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)
def runningProgram():
    if settings['restartPoint'] is not None:
        try:
            line.sendMessage(settings['restartPoint'], 'Bot can operate again ♪')
        except TalkException:
            pass
        settings['restartPoint'] = None
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)
if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()
