from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

def split_video(video_path, output_dir, segment_duration):
    """Splits a video into smaller segments.

    Args:
        video_path (str): The path to the input video file.
        output_dir (str): The directory to save the output segments.
        segment_duration (int): The duration of each segment in seconds.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video = VideoFileClip(video_path)
    duration = video.duration
    start_time = 0
    segment_num = 1

    while start_time < duration:
        end_time = min(start_time + segment_duration, duration)
        output_path = os.path.join(output_dir, f"segment_{segment_num}.mp4")
        ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_path)
        start_time = end_time
        segment_num += 1
    video.close()

if __name__ == "__main__":
    video_path = "input.mp4"  # Replace with your input video path
    output_dir = "output_segments" # Replace with your desired output directory
    segment_duration = 30 # Replace with your desired segment duration in seconds

    split_video(video_path, output_dir, segment_duration)