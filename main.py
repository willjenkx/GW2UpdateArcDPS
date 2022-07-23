from directory import check_directory, update_file
from config import setoption, initconfig
from datetime import datetime


if __name__ == '__main__':
    initconfig()
    check_directory()
    update_file()
    setoption('lastRun', "{:%B %d, %Y}".format(datetime.now()))

