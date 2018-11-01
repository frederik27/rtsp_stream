# import cv2
# from time import time, sleep
#
#
# class Camera(object):
#     def __init__(self, url):
#         self.out = cv2.VideoWriter()
#         self.cap = cv2.VideoCapture()
#         self.url = 0 if url is None else url
#
#     def get_frame(self):
#         if not self.cap.isOpened():
#             self._open()
#
#         st = time()
#         while self.cap.isOpened():
#             # sleep(0.04)
#             ret, frame = self.cap.read()
#             if ret:
#                 frame = cv2.flip(frame, 1)
#                 # self.out.write(frame)
#                 return cv2.imencode('.jpg', frame)[1].tobytes()
#             if time() - st >= 10:
#                 break
#
#     def _open(self):
#         try:
#             self.url = int(self.url)
#         except:
#             pass
#         self.cap = cv2.VideoCapture(self.url)
#         # width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         # height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         # fourcc = cv2.VideoWriter_fourcc(*'avc1')
#         # self.out = cv2.VideoWriter('video{}.mp4'.format(time()), fourcc, 20.0, (width, height))
