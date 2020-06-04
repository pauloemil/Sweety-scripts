#include <iostream>
#include<bits/stdc++.h>
using namespace std;

struct Cars{
    long ID;
    string Color;
};

struct Lanes{
    string Number;
    int FloorNumber;
    int EmptyPlaces;
    bool Full;
    float price_per_hour;
};

struct Parking{
    Cars car;
    Lanes LovationNumber;
};

int main() {
    int NumberOfPlaces = 2;
    Parking Places [NumberOfPlaces];
    while(true)
    {
        cout << endl;
        cout << "Press 1 to fill data of database." << endl;
        cout << "Press 2 to output data in the data base" << endl;
        cout << "Press 3 to search About Lanes by FloorNumber" << endl;
        cout << "Press 4 to search about cars by its ID." << endl;
        cout << "Press 5 to search about Cars by its color" << endl;
        cout << "Press 6 to search Lanes by its Number" << endl;
        cout << "Press 7 to search about Lane has empty places over 5" << endl;
        cout << "Press 8 to search about Lanes which are full" << endl;
        cout << "Press 9 to exit" << endl;
        cout << "Press 11 to show cars ID divisible by 4" << endl;
        cout << "Choice:\t";
        int choice;
        cin >> choice;
        switch(choice)
        {
        case 1:
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                long ID;
                string Color;

                string Number;
                int FloorNumber;
                int EmptyPlaces;
                string FullQuestion;
                bool Full;
                float price_per_hour;

                cout << "ID:\t";
                cin >> ID;
                cout << "Color:\t";
                cin >> Color;

                cout << "Number:\t";
                cin >> Number;
                cout << "FloorNumber:\t";
                cin >> FloorNumber;
                cout << "EmptyPlaces:\t";
                cin >> EmptyPlaces;
                cout << "Full(y/n):\t";
                cin >> FullQuestion;
                if (FullQuestion == "y")
                    Full = true;
                else
                    Full = false;
                cout << "price per hour:\t";
                cin >> price_per_hour;

                Places[i] = {{ID, Color}, {Number, FloorNumber, EmptyPlaces, Full, price_per_hour}};
            }
            break;

        case 2:
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                cout << "ID:\t" << Places[i].car.ID << endl;
                cout << "Color:\t" << Places[i].car.Color << endl;
                cout << "\nNumber:\t"<< Places[i].LovationNumber.Number << endl;
                cout << "FloorNumber:\t"<< Places[i].LovationNumber.FloorNumber << endl;
                cout << "EmptyPlaces:\t"<< Places[i].LovationNumber.EmptyPlaces << endl;
                cout << "Full:\t";
                if (Places[i].LovationNumber.Full)
                    cout << "Full" << endl;
                else
                    cout << "Empty" << endl;
                cout << "price per hour:\t"<< Places[i].LovationNumber.price_per_hour << endl;
            }
            break;
        case 3:
            {
                int FloorNumber;
                cout << "FloorNumber:\t";
                cin >> FloorNumber;
                bool Found = false;
                for (int i = 0; i < NumberOfPlaces; i++)
                {
                    if (Places[i].LovationNumber.FloorNumber == FloorNumber)
                    {
                        cout << "\nNumber:\t"<< Places[i].LovationNumber.Number << endl;
                        cout << "FloorNumber:\t"<< Places[i].LovationNumber.FloorNumber << endl;
                        cout << "EmptyPlaces:\t"<< Places[i].LovationNumber.EmptyPlaces << endl;
                        cout << "price per hour:\t"<< Places[i].LovationNumber.price_per_hour << endl;
                        Found = true;
                        break;
                    }
            }
            if (!Found)
                cout << "\nNo lanes have empty places more than 5." << endl;}
            break;
        case 4:
            {long ID;
            bool Found = false;
            cout << "ID:\t";
            cin >> ID;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].car.ID == ID)
                   {
                       Found = true;
                       cout << "ID: " << Places[i].car.ID << ", Color: " << Places[i].car.Color << endl;
                       break;
                   }
            }
            if (!Found)
                cout << "Not Found" << endl;}
            break;
        case 5:
            {string Color;
            bool Found = false;
            cout << "Color:\t";
            cin >> Color;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].car.Color == Color)
                   {
                       Found = true;
                       cout << "ID: " << Places[i].car.ID << ", Color: " << Places[i].car.Color << endl;
                       break;
                   }
            }
            if (!Found)
                cout << "Not Found" << endl;}
            break;
        case 6:
            {string Number;
            bool Found = false;
            cout << "Number:\t";
            cin >> Number;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].LovationNumber.Number == Number)
                   {
                       Found = true;
                       break;
                   }
            }
            if (Found)
                cout << "Found"<<endl;
            else
                cout << "Not Found" << endl;}
            break;
        case 7:
            {bool Found = false;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].LovationNumber.EmptyPlaces >= 5)
                   {
                        cout << "\nNumber:\t"<< Places[i].LovationNumber.Number << endl;
                        cout << "FloorNumber:\t"<< Places[i].LovationNumber.FloorNumber << endl;
                        cout << "EmptyPlaces:\t"<< Places[i].LovationNumber.EmptyPlaces << endl;
                        cout << "price per hour:\t"<< Places[i].LovationNumber.price_per_hour << endl ;
                        Found = true;
                   }
            }
            if (!Found)
                cout << "\nNo lanes have empty places more than 5." << endl;}
            break;
        case 8:
            {bool Found = false;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].LovationNumber.Full)
                   {
                        cout << "\nNumber:\t"<< Places[i].LovationNumber.Number << endl;
                        cout << "FloorNumber:\t"<< Places[i].LovationNumber.FloorNumber << endl;
                        cout << "EmptyPlaces:\t"<< Places[i].LovationNumber.EmptyPlaces << endl;
                        cout << "price per hour:\t"<< Places[i].LovationNumber.price_per_hour << endl;
                        Found = true;
                   }
            }
            if (!Found)
                cout << "\nNo lanes is full." << endl;}
            break;
        case 9:
            {exit(1);}
            break;

        case 11:
            {bool Found = false;
            for (int i = 0; i < NumberOfPlaces; i++)
            {
                if (Places[i].car.ID % 4 == 0)
                   {
                       cout << "ID: " << Places[i].car.ID << ", Color: " << Places[i].car.Color << endl;
                       Found = true;
                   }
            }
            if (!Found)
                cout << "\nNo ID of cars is divisible by 4." << endl;}
            break;
        }
    }
}



//Code to ahmed atef first cash of the game 1 / 6 / 2020
