def onAppStart(app):
    app.tempImg = Image.open('images/temp-01.png')
    app.tempImg = app.tempImg.convert('RGBA')
    nums = app.tempImg.getdata()
    newNums = []
    for item in nums:
        # if item[0] == 58 and item[1] == 84 and item[2] == 164:
        if item[0] == 61 and item[1] == 84 and item[2] == 159:
            newNums.append((255, 255, 255, 0))
        else:
            newNums.append(item)
    app.tempImg.putdata(newNums)

    tempImageWidth,tempImageHeight = app.tempImg.width,app.tempImg.height
    tempImgToPrint = CMUImage(app.tempImg)