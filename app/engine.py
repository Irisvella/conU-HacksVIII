""" Core matlab engine image processing functionality

- Process inputed data files from webapp
- Start matlab engine and eval code
- For each bounding box return an image
- return bundle of occluded images

"""
import sys
import os
import logging

import matlab.engine

def process(data):
    """Uses matlab engine to evaluate source code and produce multiple export images
    Args:
        data (dict): Bundle of data from webapp
    Returns:
        bool: True if export created existing files. False if this process failed.

    """

    # Start synchronous engine session
    core = matlab.engine.start_matlab()

    # Use detectTextCraft to create bounding boxes around extracted text only
    mat_lab_source = """
    I = imread("{path}")
    boundryBox = detectTextCRAFT(I)
    Iout = insertShape(I,"filled-rectangle", boundryBox, LineWidth=3, ShapeColor="black", Opacity=1)
    position = floor( [ (boundryBox(:,1)+boundryBox(:,3))/2,(boundryBox(:,2)+boundryBox(:,4))/2] )
    temp = sum(position');
    [val, idx] = sort(temp);
    newpositions = position(idx,:);
    RGB = insertText(Iout, newpositions(:,1:2), 1:size(newpositions,1), 'FontSize', 22, 'AnchorPoint' ,'LeftBottom');
    imwrite(RGB, "{export}")
    """.format(path=data["path"], export=data["export"])

    # Send multiline string commands to the core engine to be evaluated
    core.eval(mat_lab_source, nargout=0)
    # Check if export created modified Q&A files
    # TODO: Add multiple files functionality
    if not os.path.exists(data["export"]):
        logging.warning("Something went wrong in image export process from matlab")
        return False
    return False
