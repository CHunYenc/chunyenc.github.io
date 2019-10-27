using System;
public class hwk3_01
{
    static void Main(string[] args)
    {
        char chance = 'N';
        do
        {
            Console.Clear();
            Console.WriteLine("\n=====找出金額====\n這是一款遊戲，\n最低100元，最高900元。\n");
            Console.WriteLine("1.ear\n2.hand\n3.Leg\n4.foot\n");
            Console.Write("\n你選擇的是？(E/H/L/F)");
            Console.Write("請輸入：");
            chance = Console.ReadKey().KeyChar;
            if (chance == 'E')
            {
                Console.WriteLine("\n你選擇了耳朵。\n接下來，你要選擇左耳或右耳 (L/R)?\n");
                Console.Write("請輸入：");
                chance = Console.ReadKey().KeyChar;
                if (chance == 'L')
                {
                    Console.WriteLine("\n你選擇了左耳，你獲得200元。\n");
                }
                else if (chance == 'R')
                {
                    Console.WriteLine("\n你選擇了右耳，你獲得100元。\n");
                }
                else
                {
                    Console.WriteLine("\n輸入錯誤。\n");
                }
            }
            else if (chance == 'H')
            {
                Console.WriteLine("\n你選擇了手。\n接下來，你要選擇左手或右手 (L/R)?\n");
                Console.Write("請輸入：");
                chance = Console.ReadKey().KeyChar;
                if (chance == 'L')
                {
                    Console.WriteLine("\n你選擇了左手，你獲得500元。\n");
                }
                else if (chance == 'R')
                {
                    Console.WriteLine("\n你選擇了右手，你獲得300元。\n");
                }
                else
                {
                    Console.WriteLine("\n輸入錯誤。\n");
                }
            }
            else if (chance == 'L')
            {
                Console.WriteLine("\n你選擇了腿。\n接下來，你要選擇左腿或右腿 (L/R)?\n");
                Console.Write("請輸入：");
                chance = Console.ReadKey().KeyChar;
                if (chance == 'L')
                {
                    Console.WriteLine("\n你選擇了左腿，你獲得700元。\n");
                }
                else if (chance == 'R')
                {
                    Console.WriteLine("\n你選擇了右腿，你獲得600元。\n");
                }
                else
                {
                    Console.WriteLine("\n輸入錯誤。\n");
                }
            }
            else if (chance == 'F')
            {

                Console.Write("\n你選擇了腳。\n接下來，你要選擇左腳或右腳 (L/R)?\n");
                Console.Write("請輸入：");
                chance = Console.ReadKey().KeyChar;
                if (chance == 'L')
                {
                    Console.WriteLine("\n你選擇了左腳，你獲得900元。\n");
                }
                else if (chance == 'R')
                {
                    Console.WriteLine("\n你選擇了右腳，你獲得100元。\n");
                }
                else
                {
                    Console.WriteLine("\n輸入錯誤。\n");
                }
            }
            else
            {
                Console.WriteLine("\n都是大寫字母，請您重新輸入。\n");
            }
            Console.Write("\n你要繼續嗎？(Y/N)");
            chance = Console.ReadKey().KeyChar;
        } while (chance != 'N');
        {
            Console.WriteLine("\n離開了。\n");
        }
    }
}