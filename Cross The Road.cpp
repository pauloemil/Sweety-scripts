#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

const int width = 15;
const int hight = 20;
int x, y, score;
bool gameOver;
int carsX[hight];
int carsY[hight];
void Setup()
{
    x = width/2;
    y = 0;
    gameOver = false;
}
void Draw()
{
    system("cls");
    for (int i = 0; i < width; i++)
        cout << "-";
    cout << endl;

    for (int i = 0; i < hight; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if ( j == 0 || j == width-1)
            {
                cout << "|";
                continue;
            }

            if (j == x && i == y)
            {
                cout << "%";
                continue;
            }
            bool printed = false;
            for (int k = 0; k < hight; k++)
                if (i == carsY[k] && j == carsX[k])
                {
                    printed = true;
                    cout << ">";
                    break;
                }
            if (!printed)
                cout << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < width; i++)
        cout << "-";
    cout << endl;

}
void Input()
{
    if(_kbhit())
    {
        switch (_getch())
        {
        case 'w':
            y--;
            break;
        case 's':
            y++;
            break;
        case 'a':
            x--;
            break;
        case 'd':
            x++;
            break;
        case 'x':
            gameOver = true;
            break;
        }
    }
}

void Logic()
{
    if (x <= 0)
    {
        x = 1;
    }
    else if (x >= width-1)
    {
        x = width-2;
    }
    else if (y < 0)
    {
        y = 0;
    }
    else if (y >= hight)
    {
        score++;
        y = 0;
    }
    for ( int i = 0; i < hight; i++)
    {
        if (x == carsX[i] && y == carsY[i])
            {
                gameOver = true;

            }

    }
    int carpos = rand() % hight;
    carsY[carpos] = carpos;
    for (int i = 0; i < hight; i++)
    {
        if (carsX[i] >= width)
        {
            carsY[i] = 0;
            carsX[i] = 0;
            break;
        }
        if (carsY[i] != 0)
            carsX[i]++;

    }



}

int main()
{
    Sleep(100);
    Setup();
    while (!gameOver)
    {
        Draw();
        Input();
        Logic();
        cout << "Your Score: " << score << endl;
        //for (int i = 0; i < 10; i++)
            //cout << carsX[i] << " " <<carsY[i] << endl;
    }

    return 0;
}

// Done on 8/8/2019 7:50 PM
// paulo.busy@hotmail.com
// www.fb.com/prog.paulo
// 01554148331
