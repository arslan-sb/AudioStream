import os
import subprocess
import imageio_ffmpeg as ffmpeg_executable

input_directory = r"D:\Music\assets\audios"
output_directory = r"D:\Music\myproject\static\saqib"

def check_permissions(file_path, mode):
    """Check if the file or directory has the specified access mode."""
    return os.access(file_path, mode)

def convert_mp3_to_hls(input_path, output_directory, ffmpeg_path, segment_time=10):
    if not os.path.isfile(input_path):
        print(f"Error: Input file {input_path} does not exist or is not a file.")
        return
    
    if not check_permissions(input_path, os.R_OK):
        print(f"Error: Input file {input_path} cannot be read. Permission denied.")
        return
    
    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory)
        except PermissionError:
            print(f"Error: Cannot create output directory {output_directory}. Permission denied.")
            return
    
    if not check_permissions(output_directory, os.W_OK):
        print(f"Error: Output directory {output_directory} cannot be written to. Permission denied.")
        return

    output_file_base = os.path.join(output_directory, os.path.splitext(os.path.basename(input_path))[0])
    output_file = f"{output_file_base}.m3u8"

    command = [
        ffmpeg_path,
        '-i', input_path,
        '-codec:a', 'aac',
        '-b:a', '128k',
        '-hls_time', str(segment_time),
        '-hls_playlist_type', 'vod',
        '-hls_segment_filename', f"{output_file_base}_%03d.ts",
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Converted {os.path.basename(input_path)} to HLS.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    ffmpeg_path = ffmpeg_executable.get_ffmpeg_exe()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.mp3'):
            input_path = os.path.join(input_directory, filename)
            convert_mp3_to_hls(input_path, output_directory, ffmpeg_path)
