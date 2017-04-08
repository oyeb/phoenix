1) This API requires a library called JSON simple to be added

2) The input is a string given in one line {"bots":[{"botname":"kevin","childno":0,"radius":10,"velocity":0.59,"Xcoordinate":25,"Ycoordinate":30,"mass":20,"angle":180,"score":150},{"botname":"kevin","childno":1,"radius":90,"velocity":0.30,"Xcoordinate":5,"Ycoordinate":30,"mass":22,"angle":18,"score":150},{"botname":"juno","childno":0,"radius":90,"velocity":0.30,"Xcoordinate":23,"Ycoordinate":600,"mass":60,"angle":45,"score":90}],"maxX":14142,"maxY":14142,"food":[[1,2],[2,9],[23,35],[78,345],[89,233]],"virusrad":15,"virus":[[123,45],[3455,34],[333,77],[3455,33],[333,90],[23,55]],"ffieldcircle":[{"innerrad":30,"outerrad":45,"origin":[67,788]},{"innerrad":30,"outerrad":50,"origin":[6790,88]}],"ffieldsquare":[{"origin":[233,7888],"innerside":90,"outerside":110}]}

3) The output was [{"ejectmass":false,"split":false,"childno":0,"relativeangle":0,"pause":false},{"ejectmass":false,"split":false,"childno":1,"relativeangle":0,"pause":false}]

4) Its recommended to test this out using different inputs
