using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace hashing
{
    class Program
    {
       
        static int generatingIndex(string item, int elementsNumber)
        {
            int key = 0;
            foreach (char ch in item)
                key += (int)ch;
            int index = key % elementsNumber;
            return index;
        }
        static void InsertInFile(string item, LinkedList<string>[] myFileExample)
        {
            int elementsNumber = myFileExample.Length;
            int index = generatingIndex(item, elementsNumber);
            myFileExample[index].AddLast(item);
        }
        static bool SearchInFile(string item, LinkedList<string>[] myFileExample)
        {
            int elementsNumber = myFileExample.Length;
            int index = generatingIndex(item, elementsNumber);

            if (myFileExample[index].Contains(item))
                return true;
            return false;
        }
        static void Main(string[] args)
        {
            

            Console.Write("Enter the number of elements: ");
            int elementsNumber = int.Parse(Console.ReadLine());
            LinkedList<string>[] myFileExample = new LinkedList<string>[elementsNumber];

            for (int i = 0; i < elementsNumber; i++)
            {
                myFileExample[i] = new LinkedList<string>();
            }
            #region testing
            InsertInFile("zoe", myFileExample);
            InsertInFile("rae", myFileExample);
            InsertInFile("paulo", myFileExample);
            InsertInFile("emil", myFileExample);
            InsertInFile("omen", myFileExample);
            InsertInFile("rae", myFileExample);
            InsertInFile("paulo", myFileExample);
            InsertInFile("rae", myFileExample);
            InsertInFile("rae9", myFileExample);
            InsertInFile("paul", myFileExample);
            InsertInFile("rae", myFileExample);
            #endregion
            while (true)
            {
                Console.Write("1)\tInsert Element.\n2)\tSearch about element.\n3)\tPreview the file.\n4)\tExit.\n");
                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        Console.Write("Enter the element: ");
                        InsertInFile(Console.ReadLine(), myFileExample);
                        Console.WriteLine("Done!");
                        break;
                    case "2":
                        Console.Write("Enter the element: ");
                        if (SearchInFile(Console.ReadLine(), myFileExample))
                            Console.WriteLine("Found!");
                        else
                            Console.WriteLine("Not Found!");
                        break;
                    case "3":
                        Console.WriteLine("File:");
                        for (int i = 0; i < elementsNumber; i++)
                        {
                            Console.WriteLine(i + ")");
                            foreach (string s in myFileExample[i])
                            {
                                Console.Write(s + " - ");
                            }
                            Console.WriteLine();
                        }
                        break;
                    case "4":
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Please enter a valid choice..");
                        break;
                }
            }

        }

    }
}
