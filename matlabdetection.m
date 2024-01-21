% Get an image from textbook or photo
I = imread("C:\Users\sharo\Desktop\aheart.jpg");
oparray = [];
boundary_box = detectTextCRAFT(I);
disp(boundary_box);
Iout = insertShape(I,"filled-rectangle",boundary_box,LineWidth=3,ShapeColor="black",Opacity=1);
figure
imshow(Iout)
position = floor([(boundary_box(:,1)+boundary_box(:,3))/2,(boundary_box(:,2)+boundary_box(:,4))/2]) 
temp = sum(position');
[val, idx] = sort(temp);
newpositions = position(idx,:);
RGB = insertText(Iout, newpositions(:,1:2), 1:size(newpositions,1), 'FontSize', 22, 'AnchorPoint' ,'LeftBottom');
% Assign numbers to each bb
figure
%imshow(RGB);

imwrite(RGB,"C:\newfolderie");
