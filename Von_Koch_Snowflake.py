import turtle as tu

def segment_koch(l,n):
    flocon(l/3,n-1)
    tu.lt(60)
    flocon(l/3,n-1)
    tu.right(120)
    flocon(l/3,n-1)
    tu.lt(60)
    flocon(l/3,n-1)

def flocon(l,n) :
    if n==0 :
        tu.fd(l)
    else :
        segment_koch(l,n)

def flocon_parts (l,n):
    flocon(l,n)
    tu.lt(240)
    flocon(l,n)
    tu.lt(240)
    flocon(l,n)

if __name__ == '__main__' :
    LARGEUR, HAUTEUR = 500, 500
    tu.setup(LARGEUR, HAUTEUR)
    tu.color('green')
    tu.hideturtle()
    tu.tracer(0,0)
    tu.goto(-150,100)
    tu.fillcolor("green") 
    tu.begin_fill()
    flocon_parts (300,5)
    tu.end_fill()
    tu.exitonclick()
