import cv2

# parameters
seconds_to_add = 3
fps = 30
resolution = (1280, 720)

# define video_capture
source_video_path = r"<Video Path>" 
cap = cv2.VideoCapture(source_video_path)
ret, frame = cap.read()
print(frame.shape)

print('Calculating total number of frames...')
total_number_of_frames = 0
while True:
    ret, frame = cap.read()

    if ret:
        total_number_of_frames += 1
    else:
        break
print(f'total_number_of_frames: {total_number_of_frames}')
frames_to_add = seconds_to_add * fps
print(f'frames_to_add: {frames_to_add}')
stretch_interval = total_number_of_frames / frames_to_add
print(f'stretch_interval: {stretch_interval}')

# define video_writer
output_video_path = 'output.mp4'
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
writer = cv2.VideoWriter(output_video_path, fourcc, fps, resolution)

# write the video
cap = cv2.VideoCapture(source_video_path)
stretch_interval_counter = 0
frames_written = 0 
while True:
    if stretch_interval_counter < stretch_interval:
        ret, frame = cap.read()
        stretch_interval_counter += 1
    else:
        stretch_interval_counter = 0
    
    if ret:
        writer.write(frame)
        frames_written += 1
    else:
        break

print('Finished writing video')
print(f'original number of frames: {total_number_of_frames}')
print(f'frames_written: {frames_written}')

# close resources
cap.release()
writer.release()

