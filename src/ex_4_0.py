""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    with open(logfile) as file:
        read_lines = file.readlines()
        return [line for line in read_lines if "Shutdown initiated" in line]


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
