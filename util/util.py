import inspect
import os


def get_test_data():
    """
    Reads test_data.txt from the same folder as the file that calls this function.

    Returns:
        str: The contents of test_data.txt
    """
    # Get the frame of the caller
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename

    # Get the directory of the calling file
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Construct the path to test_data.txt
    test_data_path = os.path.join(caller_dir, 'test_data.txt')

    # Read and return the file contents
    with open(test_data_path, 'r') as f:
        return f.read()


def get_data():
    """
    Reads data.txt from the same folder as the file that calls this function.

    Returns:
        str: The contents of data.txt
    """
    # Get the frame of the caller
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename

    # Get the directory of the calling file
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Construct the path to data.txt
    data_path = os.path.join(caller_dir, 'data.txt')

    # Read and return the file contents
    with open(data_path, 'r') as f:
        return f.read()
