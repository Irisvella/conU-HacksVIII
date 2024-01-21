% Get an image from textbook or photo
I = imread("C:\Users\sharo\Desktop\aheart.jpg");
% use functionality of computer vision toolbox to detect text
boundary_box = detectTextCRAFT(I);
% print boundary box array
disp(boundary_box);
% disp(boundary_box(3,:));
%Print the blank over text field and display masked image
Iout = insertShape(I,"filled-rectangle",boundary_box,LineWidth=3,ShapeColor="black",Opacity=1);
%show figure ina  separate window
figure
imshow(Iout)

% save image to a different destination
imwrite(Iout,"C:\newfolderie\pic.jpg");

inti = 1;
for valu = 1: numel(boundary_box)/4
    Ifi = insertShape(I,"filled-rectangle",boundary_box(valu,:),LineWidth=3,ShapeColor="black",Opacity=1);
    inti = inti + 1;
    imwrite(Ifi,"C:\newfolderie\"+inti+".jpg");
end
