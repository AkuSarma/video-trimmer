from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import os

class Video_Splitter:
    def __init__(self, video_path, output_dir, segment_duration):
        self.video_path = video_path
        self.output_dir = output_dir
        self.segment_duration = segment_duration

    def get_duration(self):
        """Get video duration in seconds using OpenCV."""
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise Exception(f"Cannot open video file: {self.video_path}")
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = frame_count / fps if fps > 0 else 0
        cap.release()
        return duration

    def split(self):
        """Splits the video into segments."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        duration = self.get_duration()
        start_time = 0
        segment_num = 1

        while start_time < duration:
            end_time = min(start_time + self.segment_duration, duration)
            output_path = os.path.join(self.output_dir, f"segment_{segment_num}.mp4")
            ffmpeg_extract_subclip(self.video_path, start_time, end_time, output_path)
            start_time = end_time
            segment_num += 1

if __name__ == "__main__":
    video_path = "input.mkv"  # Replace with your input video path
    output_dir = "output" # Replace with your desired output directory
    segment_duration = 30 # Replace with your desired segment duration in seconds

    video_splitter = Video_Splitter(video_path, output_dir, segment_duration)
    video_splitter.split()