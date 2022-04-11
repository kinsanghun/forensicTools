import turtle as t

def main():

    colors = [
        "red",
        "purple",
        "blue",
        "green",
        "yellow",
        "orange"
        ]
    
    conn = t.Turtle()
    conn.speed(100)
    conn.width(3)
    length = 10

    while length < 500:
        conn.forward(length)
        conn.pencolor(colors[length%6])
        conn.right(89)
        length += 5

if __name__ == "__main__":
    main()
