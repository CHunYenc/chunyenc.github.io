using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace hwk4_1
{
    class Program
    {
        static int check_point(int n,int pick,int point)
        {

            if ( n == 0)
            {
                Console.WriteLine("已經輸入過。");
                return -1;
            }

            Console.Write("此數是 Odd 還是 Even (O|E)? ");
            char greater5 = Console.ReadKey().KeyChar;

            Console.WriteLine("\n");
            if (greater5 == 'O' || greater5 =='E'|| greater5 == 'e' || greater5 =='o')
            {
                
                if (greater5 == 'O' && n % 2 == 0 || greater5 == 'o' && n % 2 == 0)
                {
                    Console.WriteLine("你答對了是複數！");
                    return 4;
                }
                else if (greater5 == 'E' && n % 2 != 0 || greater5 == 'e' && n % 2 != 0)
                {
                    Console.WriteLine("你答對了是單數！");
                    return 4;
                }
                else
                {
                    Console.WriteLine("猜錯。");
                    return 0;
                }

            }
            else
            {
                Console.WriteLine("請重新輸入。");
            }
            return 0;
        }

        static void Main(string[] args)
        {
            int[] n = new int[4], p = new int[4];
            int pick, point = 0 , total = 0;
            Random r = new Random();

            for(int i=0;i<4;i++)
            {
                n[i] = r.Next(1, 10);
                p[i] = n[i];
            }

            Console.WriteLine("數字: * * * *");
            Console.WriteLine(n[0] + " " + n[1] + " " + n[2] + " " + n[3]);

            
            do
            {
                Console.Write("\n要猜的位數:");
                pick = Convert.ToInt32(Console.ReadLine());
                if (pick > 0 && pick < 5)
                {
                    point = check_point(n[pick - 1],pick,point);
                    n[pick - 1] = 0;
                }
                else Console.WriteLine("\n輸入錯誤。");

                if (point > 0)
                {
                    total += point;
                    Console.WriteLine("你猜中 " + point + " 分。");
                }
                else if (point == 0) Console.WriteLine("\n很可惜，你沒猜到分數。");
                Console.Write("========================================\n數字:");
                for (int i = 0; i < 4; i++) Console.Write(n[i] == 0 ? (" " + p[i]) : " * ");
            } while (n[0] != 0 || n[1] != 0 || n[2] != 0 || n[3] != 0);
            Console.WriteLine("\n\n\n結束了！你得分共 " + total + " 分");
        }
    }
}
