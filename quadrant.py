'''
in a cartesian coordinate system, a point (x,y) lies in one of four quatrants based on the sings of its x and y values

1. first quadrant(Q1)
(x>0, y<0)
2. second quadrant (Q2)
(x<0, y>0)
third quadrant (Q3)
x<0, y<0

4. fourth quadrant (x>0. y<0)

and special cases
if x==0 then lies on y axix
if y==0 then lies on x axix
and if x==0 and y==0 then lies on the origin

'''
def get_quadrant(x,y):
    if x>0 and y>0:
        return "first quadrants"
    elif x<0 and y>0:
        return "second quadrant"
    elif x<0 and y<0:
        return "third quadrant"
    elif x>0 and y<0:
        return "fourth quadrant"
    elif x==0 and y==0:
        return "origin"
    elif x==0:
        return "on the y axix"
    else:
        return "on the x axix"

x,y=map(int,input("enter coordinates(x,y)").split())
print(get_quadrant(x,y))