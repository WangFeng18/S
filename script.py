import os
import cv2
def generate_video_labels():
    video_content = '''
    <video id="video" controls="controls" preload="none" width="300" height="300" poster='{}'>
          <source id="mp4" src="{}" type="video/mp4">
          <p>Your user agent does not support the HTML5 Video element.</p>
    </video>
    '''
    content = ''
    for fn in os.listdir('./'):
        if fn.endswith('_scaled.mp4'):
            content += video_content.format(fn.replace('.mp4', '.jpg'), fn)
    with open('temp.txt', 'w+') as f:
        f.writelines(content)
            
def extract_poster():
    for fn in os.listdir('./'):
        if fn.endswith('_scaled.mp4'):
            cap = cv2.VideoCapture(fn)
            ret, frame = cap.read()
            cv2.imwrite(fn.replace('.mp4', '.jpg'), frame)
            print(frame.shape)

def scale_video():
    for fn in os.listdir('./'):
        if fn.endswith('.mp4') and not fn.endswith('_scaled.mp4'):
            #ffmpeg -i video--7T50tAIrg_epoch_0.mp4 -vf scale=300:300 -aspect 1:1 -acodec aac -vcodec h264 -max_muxing_queue_size 1024 out.mp4
            cmd = 'ffmpeg -i {} -vf scale=300:300 -aspect 1:1 -acodec aac -vcodec h264 -max_muxing_queue_size 1024 {}'.format(fn, fn.replace('.mp4', '_scaled.mp4'))
            os.system(cmd)
#scale_video()
generate_video_labels()
extract_poster()
