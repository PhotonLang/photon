OPEN 'test.png' AS image
APPLY 'solarize' TO image
SAVE image TOSYS 'output.png'
CLOSE image