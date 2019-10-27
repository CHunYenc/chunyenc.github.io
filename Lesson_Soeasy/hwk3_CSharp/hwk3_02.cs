using System;

namespace hwk3_02
{
    class Program
    {
        static void Title()
        {
            Console.WriteLine("=================================================");
            Console.WriteLine("製作：B10610020");
            Console.WriteLine("歡迎來到命運轉盤。");
            Console.WriteLine("-------------------------------------------------");
            Console.WriteLine("1.再抽一次。");
            Console.WriteLine("2.銘謝惠顧。");
            Console.WriteLine("3.MacBook Pro 13");
            Console.WriteLine("4.銘謝惠顧。");
            Console.WriteLine("5.銘謝惠顧。");
            Console.WriteLine("6.銘謝惠顧。");
            Console.WriteLine("7.Nokia 5.1 Plus");
            Console.WriteLine("8.銘謝惠顧。");
            Console.WriteLine("9.Jabra Elite 65t 真無線藍牙耳機");
            Console.WriteLine("10.再抽一次。");
            Console.WriteLine("=================================================");
        }

        static void Run(int number,int count)
        {
            char chance = 'o';
            if (number == 0)
            {
                Console.WriteLine("\n你沒機會了。");
            }
            else if (chance =='n')
            {
                Console.WriteLine("\n離開。");
            }


            else
            {
                Console.Write("現在遊玩嗎？(y/n)");
                chance = Console.ReadKey().KeyChar;
                Random r = new Random();
                int x = r.Next(1, 10);
                switch (x)
                {
                    case 3:
                        count+=1;
                        number-=1;
                        Console.WriteLine("\n=================================================");
                        Console.WriteLine("\n第 " + count + " 次機會。" + "你抽到 " + x + " 號。\n恭喜！抽到 MacBook Pro 13。");
                        Console.WriteLine("你還有 " + number + " 次機會。");
                        Console.WriteLine("=================================================");
                        Run(number,count);
                        break;
                    case 7:
                        count += 1;
                        number -= 1;
                        Console.WriteLine("\n=================================================");
                        Console.WriteLine("\n第 " + count + " 次機會。" + "你抽到 " + x + " 號。\n恭喜！抽到 Nokia 5.1 Plus。");
                        Console.WriteLine("你還有 " + number + " 次機會。");
                        Console.WriteLine("=================================================");
                        Run(number, count);
                        break;
                    case 9:
                        count += 1;
                        number -= 1;
                        Console.WriteLine("\n=================================================");
                        Console.WriteLine("\n第 " + count + " 次機會。" + "你抽到 " + x + " 號。\n恭喜！抽到 Jabra Elite 65t 真無線藍牙耳機。");
                        Console.WriteLine("你還有 " + number + " 次機會。");
                        Console.WriteLine("=================================================");
                        Run(number, count);
                        break;
                    case 2:
                    case 4:
                    case 5:
                    case 6:
                    case 8:
                        count += 1;
                        number -= 1;
                        Console.WriteLine("\n=================================================");
                        Console.WriteLine("\n第 " + count + " 次機會。" + "你抽到 " + x + " 號。\n抽到銘謝惠顧。");
                        Console.WriteLine("你還有 " + number + " 次機會。");
                        Console.WriteLine("=================================================");
                        Run(number,count);
                        break;
                    case 1:
                    case 10:
                        count += 1;
                        Console.WriteLine("\n=================================================");
                        Console.WriteLine("\n第 " + count + " 次機會。" + "你抽到 " + x + " 號。\n抽到再抽一次。");
                        Console.WriteLine("你還有 " + number + " 次機會。");
                        Console.WriteLine("=================================================");
                        Run(number,count);
                        break;
                }
            }
            
        }

        static void Main(string[] args)
        {
            int number,count=0;
            char co = 'o';
            do
            {
                Console.Clear();
                Title();

                Console.Write("遊玩一次500元，\n請問你要遊玩幾次呢？");
                number = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("你要遊玩 " + number + " 次，總共花費為：" + number * 500 + "元");
                Console.WriteLine("=================================================");
                Run(number, count);
                Console.Write("還想繼續玩嗎？(y/n)");
                co = Console.ReadKey().KeyChar;
            } while (co != 'n');
            
        }
    }
}
