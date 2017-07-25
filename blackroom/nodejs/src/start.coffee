superagent = require 'superagent'
fs = require 'fs'
path = require 'path'
os = require 'os'
UA = "Mozilla/5.0 (Windows NT 6.1) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) " +
    "Chrome/55.0.2883.87 Safari/537.36"
saveTo = ""
fileSaveTo = ""
console.log "OS:" + os.platform()
switch os.platform()
    when "win32"
        saveTo = path.resolve(__dirname, ".\\data\\")
        fileSaveTo = saveTo + "\\blackroom.json"
    else
        saveTo = path.resolve(__dirname, "./data/")
        fileSaveTo = saveTo + "/blackroom.json"
blackjson = []
getData = (originType = 0) ->
    link = "https://www.bilibili.com/blackroom/web/blocked_info?originType=" +
        originType + "&pageSize=0"
    console.log link
    console.log "Downloading..."
    superagent.get link
        .set 'User-Agent', UA
        .end (err, sres) ->
            if err
                console.log "====失败(错误代码:" + sres.status.toString() + ")"
                console.log "重试..."
                getData originType
                return
            else
                dataJson = sres.body
                if dataJson.code == 0
                    blackjson = dataJson.data
                    if blackjson.length > 0
                        console.log "====共" + blackjson.length.toString() +
                            "个数据"
                        console.log "Saving..."
                        saveData JSON.stringify blackjson
                        console.log "END"
                        process.exit()
                    else
                        console.log "数据空白(0个)"
                    return
                else
                    console.log "===失败(" + dataJson.msg + ")"
                    console.log "重试..."
                    getData originType
                    return
    return
addItem = (pageData) ->
    newList = []
    newList = blackjson.concat pageData
    console.log "列表从" + blackjson.length.toString() +
        "个增加到" + newList.length.toString() + "个"
    blackjson = newList
    return

saveData = (data) ->
    console.log "Mkdir " + saveTo
    console.log "Save to " + fileSaveTo
    fs.exists saveTo, (exists) ->
        if !exists
            fs.mkdir saveTo
        return
    return
saveFile = (filePath, fileData) ->
    fs.open filePath, 'a', (err, fd) ->
        if err
            console.error err
            return
        else
            buffer = new Buffer data
            fs.write fd, buffer, 3, 9, 12,  (err, written, buffer) ->
            if err
                console.log '写入文件失败'
                console.error(err)
                return
            else
                console.log buffer.toString()
                fs.write fd, buffer, 12, 9, null, (err, written, buffer) ->
                    console.log buffer.toString()
                    return
            return
console.log "Start"
getData()