import os
import re
import shutil
import sys
from logging import NullHandler, getLogger

import matplotlib.pyplot as plt
from base_pyfile import (
    get_files,
    get_log_handler,
    make_logger,
    read_text_file,
    unique_path,
    write_file,
)

from relearning import reannotation

logger = getLogger("log").getChild(__name__)
logger.addHandler(NullHandler())


class LineGraph:
    """_summary_

    Returns:
        str: _description_
    """

    def __init__(self, title="", xlabel="", ylabel="") -> None:
        self.fig = plt.figure(figsize=(100, 10), facecolor="white")
        self.ax = self.fig.add_subplot(111, xlabel=xlabel, ylabel=ylabel, title=title)
        logger.info(f"タイトル{title}で折れ線グラフを作ります")

        self.firstlinecreate = False

    def line_create(self, line_list, label="", x_line=[]):
        if not self.firstlinecreate:
            if x_line:
                self.x_line = x_line
            else:
                self.x_line = [e for e in range(len(line_list))]
            self.firstlinecreate = True
            self.ax.plot(self.x_line, line_list, label=label)

        else:
            if len(line_list) > len(self.x_line):
                print("error")
            self.ax.plot(line_list, label=label)

        logger.debug(f"{label}ラベルで作成")

    def save(self, save_path="image"):
        os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
        self.ax.legend()
        self.fig.savefig(unique_path(f"{save_path}.png"))
        logger.info(f"{save_path}.pngとして折れ線グラフを保存しました")


def yolo_conf(label_folder, extract=1, width=1280):
    coordinate = []
    for i in get_files(label_folder):
        x = reannotation(i)
        if x:
            y = int(float(x.split()[extract]) * width)
        coordinate.append(y)

    write_text = "\n".join(str(c) for c in coordinate)
    write_file(extract, write_text)

    return coordinate


def confer(label_folder):
    zz = []
    for i in read_text_file(label_folder, "\n"):
        if i and float(i) > 0:
            zz.append(float(i) * 100)
        elif float(i) < 0:
            zz.append(0)
    return zz


def create_yolo_graph(labels_path=""):
    sample_list = []
    sample_list.append(yolo_conf(labels_path))
    sample_list.append(yolo_conf(labels_path, 2, 720))
    sample_list.append(confer(r"C:\tool\yolo_agent\yolo_agent\anomaly_score.txt"))
    sample_list.append(confer(r"C:\tool\yolo_agent\yolo_agent\anomaly_scores.txt"))
    

    LG = LineGraph()

    process = [lambda x=list: LG.line_create(x) for list in sample_list]

    for graph in process:
        graph()

    LG.save()


import matplotlib.pyplot as plt


def create_graph(data_list):
    """
    Creates a simple line graph from a list of data.

    Args:
    - data_list: a list of data points to be plotted

    Returns:
    - None
    """
    # Set up the plot
    plt.plot(data_list)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    logger = make_logger(handler=get_log_handler(20))

    create_yolo_graph(r"F:\AI_project_y\新しいフォルダー\labels")
