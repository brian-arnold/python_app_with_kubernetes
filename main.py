import sys
import os

def main():
    
    try:
        input_file = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python main.py <input_file>")

    file_number = os.path.basename(input_file)
    file_number = file_number.replace('.txt', '').replace('input_file', '')

    with open(input_file, 'r') as f:
        data = f.readlines()
        print(file_number, len(data))
        # /data here is the volume that is mounted to the container
        with open(f'/data/output_file{file_number}.txt', 'w') as f:
            for line in data:
                f.write(line[0:4]+ "\n")

if __name__ == '__main__':
    main()
