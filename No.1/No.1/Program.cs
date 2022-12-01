using System.Security.Cryptography.X509Certificates;
using System.Xml.Schema;

namespace No._1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> outputs = new List<int>();
            int currcnt = 0;

            foreach (var calories in File.ReadAllText("Input.txt").Split("\r\n"))
            {
                if (!string.IsNullOrEmpty(calories))
                {
                    currcnt += int.Parse(calories);
                }
                else
                {
                    outputs.Add(currcnt);
                    currcnt = 0;
                }
            }

            var ordered = outputs.OrderByDescending(x => x).ToList();
            
            Console.WriteLine($"Top Elf Calories: {ordered.First()}");
            Console.Write($"Top 3 Elf Calories: {ordered.Take(3).Sum()}");
            Console.ReadLine();
        }
    }
}