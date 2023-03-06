import cairo
import math
import argparse
import os
import re
import sys
import datetime
from collections import defaultdict
import pandas as pd

def read_data(filename):
    """Read data from the file and return a list of tuples.
    """
    with open(filename, 'r') as f:
        data = f.read().split("\n")

    # save data into dictionary
    #{job_name: (start_time, end_time)}
    data_dict = defaultdict(list)
    for line in data:
        line = line.split(',')
        try:
            start_time = pd.to_datetime(line[1], format='%d-%m-%Y %H:%M:%S')
            end_time = pd.to_datetime(line[2], format='%d-%m-%Y %H:%M:%S')
        except:
            continue
        # print (start_time, end_time)
        job_time = (start_time, end_time)
        data_dict[line[0]].append(job_time)

    return data_dict


def cairo(data):
    """
    Draw a timeline using cairo.
    """
    
    width = 1000
    height = 1000

    # create a surface to draw on
    surface = cairo.surfaces.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    # surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    # create a cairo context
    ctx = cairo.Context(surface)

    # draw a white background
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

    # draw a black border
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(0, 0, width, height)
    ctx.stroke()


    # draw a red line
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(2)
    ctx.move_to(0, 0)
    ctx.line_to(width, height)
    ctx.stroke()




def main():
    path = "dataset/data.txt"
    data = read_data(path)

    cairo(data)
    # play(data)

main()