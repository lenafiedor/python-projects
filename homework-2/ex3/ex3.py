import os

def get_file_stats(folder_path):
    largest_size = 0
    smallest_size = float('inf')
    newest_file = None
    newest_timestamp = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_timestamp = os.path.getmtime(file_path)

            if file_size > largest_size:
                largest_size = file_size
            if file_size < smallest_size:
                smallest_size = file_size

            if file_timestamp > newest_timestamp:
                newest_timestamp = file_timestamp
                newest_file = file

    return largest_size, smallest_size, newest_file

if __name__ == '__main__':

    folder_path = os.path.dirname(os.path.abspath(__file__)) + '/bitwy'
    print(folder_path)
    largest, smallest, newest = get_file_stats(folder_path)
    print(f'Largest file size: {largest}')
    print(f'Smallest file size: {smallest}')
    print(f'Newest file name: {newest}')
