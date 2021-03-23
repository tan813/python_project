# import  random
# from PIL import Image, ImageDraw, ImageFont
# #Pillow模块处理图片
# #产生随机字母:
# def rndChar():
#     return chr(random.randint(65,97))
# #产生随机颜色1:
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#
# #产生随机颜色2:
# def rndColor2():
#     return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#
# #定义图片尺寸
# width=60*4
# height=60
# image=Image.new('RGB',(width,height),(255,255,255))
# #创建字体Font对象：
# #该方法从指定的文件加载了一个字体对象，并且指定字体大小
# f_ont=ImageFont.truetype('arial.ttf',36)
#
# #创建Draw对象:
# #创建一个可用来对image进行操作的对象。对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建
# draw=ImageDraw.Draw(image)
#
# #填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())
#
# #输出文字:
# for t in range(4):
#     draw.text((60*t+10,10),rndChar(),fill=rndColor2(),font=f_ont)
# image.show()



from turtle import *
# def drawstart(x,y):
#    pu()
#    goto(x,y)
#    pd()
#    seth(30)#设置朝向
#    color(1,0,0)#RGB所占比
#    begin_fill()
#    for i in range(5):
#        fd(40)
#        rt(144)
#    end_fill()
# for x in range(0,100,50):
#     drawstart(x,0)
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

# for x in range(1,9):
#     forward(50)
#     rt(225)
# done()

seth(30)
for i in range(0,4):
    fd(50)
    lt(30)
    fd(50)
    rt(120)
done()