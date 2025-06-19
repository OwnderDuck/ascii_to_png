from PIL import Image, ImageDraw

# 输入字符画（注意对齐）
char_art = """        ##      ####
     ###########....###
    #.......##..#.....#
   #...#...##......###
   ##...####.#######
    ####............##
    #................#
   #.................#
  #..................#
 ############........#
 ###.................#
    ##...............##
    ##...............###
   # #...............# ##
  #  #................# #
 #   #................#  #
##   #................#  ##
 #   #................#  #
  #  #................# ##
  # #.................##
   ##.................#
   ##.................#
    #.................#
    #.................#
    #..................#
    #..................#
    #..................#
   #..................#
   #..................#
   ####################
   #                   #
   #                   #
   #                   #
   #                   #
   #                   #
   #                   #
   #                   #
   #                  #
   #                  #
  ##                  ###"""


# 预处理字符画

lines = char_art.split('\n')# [line.rstrip() for line in char_art.strip().split('\n')]
max_width = max(len(line) for line in lines)

# 创建图片
img_width = max_width
img_height = len(lines)
image = Image.new('RGBA', (img_width, img_height), (0,0,0, 0))
draw = ImageDraw.Draw(image)

# 绘制像素块
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            draw.rectangle([x, y, x, y], fill=(0,0,0))
        elif char == '.':
            draw.rectangle([x, y, x, y], fill=(255,255,255))

# 保存图片
image.save(input()+'.png');
image.show()  # 预览图片
