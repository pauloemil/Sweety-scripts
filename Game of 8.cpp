#include <iostream>
#include <conio.h>
#include <windows.h>
#include <vector>
using namespace std;


bool gameover;
const int gsize = 3;
int x;
int y;
int tempX, tempY;
int item;
vector <vector <int> > vec = {{4, 7, 6}, {1, 8, 3}, {2, 5, 0}};
int arr[3][3] = {{1,2,3}, {4,5,6}, {7,8,0}};
void setup()
{
    gameover = false;
    x = 2;
    y = 2;
}

void draw()
{
    system("cls");
    cout << "Your aim is to rearrange me like that!" << endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
    cout << endl;
    cout << endl;

    for (int i = 0; i < 3; i ++)
    {
        for (int j = 0; j < 3; j++)
            {
                if (vec[i][j] == 0)
                cout << "  ";
                else
                    cout <<vec[i][j] << " ";
            }
        cout << endl;
    }

}

void logic()
{
    if (tempX > 2)
        tempX--;
    else if (tempY > 2)
        tempY--;
    else if (tempY < 0)
        tempY++;
    else if (tempX < 0)
        tempX++;
    if (x > 2)
        x--;
    else if (y > 2)
        y--;
    else if (y < 0)
        y++;
    else if (x < 0)
        x++;
    swap(vec[x][y], vec[tempX][tempY]);

}

void input()
{
    tempX = x;
    tempY = y;
    if (_kbhit())
    {
        switch (_getch())
        {
            case 'w':
                x--;
                break;
            case 's':
                x++;
                break;
            case 'a':
                y--;
                break;
            case 'd':
                y++;
                break;
            case 'x':
                gameover = true;
                break;
        }
    }
}



int main()
{
    setup();


    while (!gameover)
    {
        input();
        logic();
        draw();
        cout << "(" << x << ", " << y << ")";
    }

}

