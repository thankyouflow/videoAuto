import os
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

#영상자르기
# os.system("ffmpeg -i /Users/realizer/Documents/youtubeDown/target.mp4 -ss 120 -to 127 /Users/realizer/Documents/youtubeDown/output.mp4")

#영상넓이 자르기
# os.system('ffmpeg -i /Users/realizer/Documents/youtubeDown/output.mp4 -vf "pad=1920:1920:(ow-iw)/2:(oh-ih)/2:black" /Users/realizer/Documents/youtubeDown/test.mp4')

os.system('ffmpeg -i /Users/realizer/Documents/youtubeDown/test.mp4 -vn /Users/realizer/Documents/youtubeDown/test.mp3')

video_output_path = '/Users/realizer/Documents/youtubeDown/text.mp4'
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

cap = cv2.VideoCapture('/Users/realizer/Documents/youtubeDown/test.mp4')

vid_fps = cap.get(cv2.CAP_PROP_FPS )
vid_size = (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

vid_writer = cv2.VideoWriter(video_output_path, codec, vid_fps, vid_size)

while(True):
    ret, frame = cap.read()
    if not ret:
        print('더 이상 처리할 frame이 없습니다.')
        break
    b, g, r, a = 255, 255, 255, 0
    fontpath = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    font = ImageFont.truetype(fontpath, 80)
    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    text = "우에우에"
    byText = "출처 : 오토"
    draw.text((img_pil.size[0]/2 - len(text) / 2 * 62, 440), text, font=font, fill=(b, g, r, a))
    draw.text((img_pil.size[0]/2 - len(byText) / 2 * 50, 1440), byText, font=font, fill=(b, g, r, a))
    img = np.array(img_pil)

    vid_writer.write(img)

vid_writer.release()
cap.release()

os.system('ffmpeg -i /Users/realizer/Documents/youtubeDown/text.mp4 -i /Users/realizer/Documents/youtubeDown/test.mp3 -c:v copy -c:a aac -strict experimental /Users/realizer/Documents/youtubeDown/result.mp4')