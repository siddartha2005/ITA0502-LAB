import cv2

def reverse_video(input_video, output_video):

    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error: Cannot open sample.mp4")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("Error: No frames found in video")
        return

    frames.reverse()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        output_video,
        fourcc,
        fps,
        (width, height)
    )

    if not out.isOpened():
        print("Error: Cannot create output video")
        return

    for frame in frames:
        out.write(frame)

    out.release()

    print("Reverse video created successfully!")
    print("Output file:", output_video)
    print("Total frames:", len(frames))

reverse_video('sample.mp4', 'reverse_video.mp4')
