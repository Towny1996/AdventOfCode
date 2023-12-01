
namespace No._10
{
    internal class Program
    {

        private static Dictionary<int, string> cycleQueue = new Dictionary<int, string>();
        private static Dictionary<int, int> cycleStrengths = new Dictionary<int, int>();
        private static int x = 1;

        static void Main(string[] args)
        {
            int iteration = 1;
            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                Console.WriteLine(iteration);
                var commands = line.Split(' ');

                switch (commands[0])
                {
                    case "addx":
                        cycleQueue.Add(iteration + 2, commands[1]);
                        break;
                }

                if (iteration is 20 or 60 or 100 or 140 or 180 or 220)
                {
                    cycleStrengths.Add(iteration, x * iteration);
                }

                CheckIterationTasks(iteration);
                iteration++;
            }
            
            Console.WriteLine(x);
            Console.ReadLine();
        }

        private static void CheckIterationTasks(int iteration)
        {
            if (cycleQueue.ContainsKey(iteration))
            {
                switch (cycleQueue.First(x => x.Key == iteration).Value[0])
                {
                    case '-':
                        x -= int.Parse(cycleQueue.First(x => x.Key == iteration).Value.Substring(1));
                        break;
                    default:
                        x += int.Parse(cycleQueue.First(x => x.Key == iteration).Value);
                        break;
                }

                cycleQueue.Remove(iteration);
            }
        }
    }
}