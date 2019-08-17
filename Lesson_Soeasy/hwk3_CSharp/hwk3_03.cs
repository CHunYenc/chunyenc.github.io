using System;

namespace hwk3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the expession: ");
            string[] exp = Console.ReadLine().Split(' ');
            double a = Convert.ToInt32(exp[0]), b = Convert.ToInt32(exp[2]);
            double c = Convert.ToInt32(exp[4]), d = Convert.ToInt32(exp[6]);
            char op1 = exp[1][0], op2 = exp[3][0], op3 = exp[5][0];
            if (op1 == '/' && op2 == '+' && op3 == '/') Console.WriteLine(a + "/" + b + " + " + c + "/" + d + " = " + ((a * d) + (b * c)) + "/" + (b * d));
            if (op1 == '/' && op2 == '-' && op3 == '/') Console.WriteLine(a + "/" + b + " - " + c + "/" + d + " = " + ((a * d) - (b * c)) + "/" + (b * d));
            if (op1 == '/' && op2 == '*' && op3 == '/') Console.WriteLine(a + "/" + b + " * " + c + "/" + d + " = " + (a * c) + " * " + (b * d));
            if (a == 0 || c == 0) Console.WriteLine(a + "/" + b + " / " + c + "/" + d + " is undefined.");
            else if (op1 == '/' && op2 == '/' && op3 == '/')
            {
                Console.WriteLine(a + "/" + b + " / " + c + "/" + d + " = " + (a * d) + " / " + (b * c));
            }
        }
    }
}
