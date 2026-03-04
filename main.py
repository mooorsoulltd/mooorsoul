import argparse
import os


def process_video(file_path):
    # Placeholder function for processing a video file.
    print(f'Processing video: {file_path}')


def main():
    parser = argparse.ArgumentParser(description='Video Analysis Application')
    parser.add_argument('video_files', nargs='+', help='List of video files to process')
    
    args = parser.parse_args()
    
    for video_file in args.video_files:
        if os.path.isfile(video_file):
            process_video(video_file)
        else:
            print(f'File not found: {video_file}')

if __name__ == '__main__':
    main()