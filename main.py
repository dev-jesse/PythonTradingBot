import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient

from pprint import pprint

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

if __name__ == '__main__':
    binance = BinanceFuturesClient("ab14d55f3d8e765daeea21d5cab2f1ef87b55f0ade917004046a4095621e21f3",
                                   "5d00ebd9aef569f138668424aa1b252999e9ccf1264e4693c0c4f25f31dff0bb", True)
    root = tk.Tk()
    root.mainloop()
