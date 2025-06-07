from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

class Video_Splitter:
    def __init__(self, video_path, output_dir, segment_duration):
        self.video_path = video_path
        self.output_dir = output_dir
        self.segment_duration = segment_duration

    def split(self):
        """Splits the video into segments."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        video = VideoFileClip(self.video_path)
        duration = video.duration
        start_time = 0
        segment_num = 1

        while start_time < duration:
            end_time = min(start_time + self.segment_duration, duration)
            output_path = os.path.join(self.output_dir, f"segment_{segment_num}.mp4")
            ffmpeg_extract_subclip(self.video_path, start_time, end_time, targetname=output_path)
            start_time = end_time
            segment_num += 1
        video.close()


if __name__ == "__main__":
    video_path = "input.mkv"  # Replace with your input video path
    output_dir = "output/output_segments" # Replace with your desired output directory
    segment_duration = 30 # Replace with your desired segment duration in seconds

    video_splitter = Video_Splitter(video_path, output_dir, segment_duration)
    video_splitter.split()