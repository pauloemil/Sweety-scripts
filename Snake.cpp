#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

bool gameOver;
const int width = 20, hight = 20;
int x, y, fruitX, fruitY, Score;
int tailX[100], tailY[100];
int tailN = 0;
char dir;

void Setup()
{
    gameOver = false;
    x = width/2;
    y = hight/2;
    fruitX = rand() % width;
    fruitY = rand() % hight;
    Score = 0;


}

void Draw()
{
    system("cls");
    for (int i = 0; i < width+1; i++)
        cout << "-";
    cout << endl;

    for (int i = 0; i < hight; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j == 0 || j == width -1)
                cout << "|";
            if (i == y && j == x)
                cout << "0";
            else if (i == fruitY && j == fruitX)
                cout << "$";
            else
            {
                bool printed = false;
                for (int k = 0; k < tailN; k++)
                {

                    if (tailX[k] == j && tailY[k] == i)
                    {
                        printed = true;
                        cout << "o";
                    }

                }
                if (!printed)
                    wcout << " ";

            }
        }
        cout << endl;
    }

    for (int i = 0; i < width+1; i++)
        cout << "-";
    cout << endl;
    cout << "Your Score: " << Score << endl;
}

void Input()
{
    if (_kbhit())
    {
        switch (_getch())
        {
        case 'a':
            dir = 'L';
            break;
        case 'w':
            dir = 'U';
            break;
        case 'd':
            dir = 'R';
            break;
        case 's':
            dir = 'D';
            break;
        case 'x':
            gameOver = true;
            break;

        }
    }
}

void Logic()
{
    int prevX = tailX[0], prevY = tailY[0];
    int prevX2, prevY2;
    tailX[0] = x;
    tailY[0] = y;
    for (int i = 1; i < tailN; i++)
    {
        prevX2 = tailX[i];
        prevY2 = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prevX2;
        prevY = prevY2;
    }
    switch (dir)
    {
    case 'L':
        x--;
        break;
    case 'R':
        x++;
        break;
    case 'U':
        y--;
        break;
    case 'D':
        y++;
        break;
    default:
        break;
    }
    // to make the borders kill the snake.
    //if (x >= width-1 || x < 0 || y >= hight || y < 0)
        //gameOver = true;
    if (x >= width-1)
        x = 0;
    else if (x <= 0)
        x = width-2;
    else if (y >= hight)
        y = 0;
    else if (y < 0)
        y = hight;
    for (int i = 0; i < tailN; i++)
        if (tailX[i] == x && tailY[i] == y)
            gameOver = true;

    if (x == fruitX && y == fruitY)
    {
        Score += 10;
        fruitX = rand() % width;
        fruitY = rand() % hight;
        tailN++;
    }

}

int main()
{
    Setup();
    while (!gameOver)
    {
        Draw();
        Input();
        Logic();
        Sleep(20);
    }
    return 0;
}
// Done on 8/8/2019 10:05 AM
// paulo.busy@hotmail.com
// www.fb.com/prog.paulo
// 01554148331
