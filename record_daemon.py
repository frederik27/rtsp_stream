import os
import cv2
from time import time
from datetime import date, datetime


def record_daemon():
    cap = cv2.VideoCapture('rtsp://109.188.128.30:5542/s1')
    # cap = cv2.VideoCapture(0)
    while True:
        cam_name = 'Camera 1'
        dirs = 'videos/{}/{}'.format(cam_name, date.today())
        file_name = '{}.mp4'.format(date.strftime(datetime.today(), '%H-%M-%S'))
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        path_to_file = os.path.relpath('{}/{}'.format(dirs, file_name))
        # current_frame = 0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(path_to_file, fourcc, 20.0, (width, height))
        frame_time, start_time = time(), time()
        while cap.isOpened():
            _, frame = cap.read()
            out.write(frame)
            if time() - frame_time >= 600:
                cv2.imwrite('frames/{}.jpg'.format(cam_name), frame)
                frame_time = time()
            if time() - start_time >= 10:
                break
                # current_frame += 1
        out.release()


if __name__ == '__main__':
    record_daemon()
