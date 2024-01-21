""" Core matlab process functionality 

- Process inputed data files from webapp
- Start matlab engine and eval code 
- For each bounding box return an image  
- return bundle of occluded images 

"""
import sys 

import matlab.engine
core = matlab.engine.start_matlab()

def process(data):
    # Start synchronous engine session 
    core = matlab.engine.start_matlab()
    # Use detectTextCraft to create bounding boxes around extracted text only
    matLabSource = """
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
    # Send multilien string commands to the core engine to be evaluated
    core.eval(matLabSource, nargout=0)

if __name__ == "__main__":
    try:
        process(data=sys.argv[1])
    except IndexError:
         # TODO: remove hardcode value and take sys.argv[0] of webapp input temp image
        data = {"path": "/home/kp/Downloads/hyrdrophilic.jpeg",
                "export": "/home/kp/Downloads/test.jpeg"}
        process(data)
