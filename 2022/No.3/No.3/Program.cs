using System.Net.NetworkInformation;
using static System.Formats.Asn1.AsnWriter;

namespace No._3
{
    internal class Program
    {
        private const string Alphabet = "abcdefghijklmnopqrstuvwxyz";

        static void Main(string[] args)
        {
            Pt1();
            Pt2();

            Console.Read();
        }

        public static void Pt1()
        {
            int score = 0;

            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                var s1 = line.Substring(0, line.Length / 2);
                var s2 = line.Substring(line.Length / 2, line.Length / 2);

                var uniqueCharsS1 = s1.Distinct();
                var uniqueCharsS2 = s2.Distinct();

                var commonItems = uniqueCharsS1.Intersect(uniqueCharsS2).ToList();
                
                score += CalcPriorityScore(commonItems.First());
            }

            Console.WriteLine(score);
        }

        public static void Pt2()
        {
            int score = 0;
            List<string> group = new List<string>();

            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                group.Add(line);

                if (group.Count != 3)
                    continue;

                var common = group[0].Intersect(group[1]).Intersect(group[2]);

                score += CalcPriorityScore(common.First());

                group.Clear();
            }

            Console.WriteLine(score);
        }

        private static int CalcPriorityScore(char item)
        {
            var priorityScore = Alphabet.IndexOf(item);
            if (priorityScore == -1)
            {
                priorityScore = Alphabet.ToUpper().IndexOf(item);
                return 27 + priorityScore;
            }
            else
            {
                return 1 + priorityScore;
            }
        }
    }
}