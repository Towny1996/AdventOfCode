namespace No._2
{
    internal class Program
    {
        private static Dictionary<string, string> pm = new Dictionary<string, string> { { "X", "A" }, { "Y", "B" }, { "Z", "C" } };
        private static Dictionary<string, string> wc = new Dictionary<string, string> { { "A", "C" }, { "B", "A" }, { "C", "B" } };
        private static Dictionary<string, string> lc = new Dictionary<string, string> { { "A", "B" }, { "B", "C" }, { "C", "A" } };
        private static Dictionary<string, int> pp = new Dictionary<string, int> { {"A", 1}, {"B", 2}, {"C", 3} };

        static void Main(string[] args)
        {
            Pt1();
            Pt2();

            Console.ReadLine();
        }

        static void Pt1()
        {
            int score = 0;

            foreach (var l in File.ReadAllLines("Input.txt"))
            {
                var m = l.Split(" ");
                var c = m[0];
                var p = pm[m[1]];

                score += pp[p];
                score += p == wc[c] ? 0 : p == c ? 3 : 6;
            }

            Console.WriteLine($"Total Score for Pt1: {score}");
        }

        static void Pt2()
        {
            int score = 0;

            foreach (var l in File.ReadAllLines("Input.txt"))
            {
                var m = l.Split(" ");
                var c = m[0];
                var p = m[1] == "Y" ? c : m[1] == "Z" ? lc[c] : wc[c];

                score += pp[p];
                score += p == wc[c] ? 0 : p == c ? 3 : 6;
            }

            Console.WriteLine($"Total Score for Pt2: {score}");
        }
    }
}