using System.Security.Cryptography.X509Certificates;

namespace No._7
{
    internal class Program
    {
        private static Node Directory = new Node(null);
        private static List<long> LargeDirectories = new List<long>();
        private static List<long> AllDirectorySizes = new List<long>();

        static void Main(string[] args)
        {
            PopulateNodeStructure();
            CalcDirectorySizes(Directory);

            Console.WriteLine($"Part 1: {LargeDirectories.Sum()}");
            Console.WriteLine($"Part 2: {GetDirectorySizeToDelete()}");
        }

        private static void PopulateNodeStructure()
        {
            Node CurrentNode = Directory;

            foreach (string line in File.ReadAllLines("Input2.txt"))
            {
                if (line.StartsWith("$"))
                {
                    var command = line.Split(" ");

                    if (command[1] == "cd" && command[2] == "..")
                    {
                        CurrentNode = CurrentNode.PreviousNode;
                    } 
                    else if (command[1] == "cd" && command[2] != "..")
                    {
                        var nextDir = new Node(CurrentNode)
                        {
                            DirName = command[2]
                        };

                        CurrentNode.Children.Add(nextDir);
                        CurrentNode = nextDir;
                    }
                }
                else
                {
                    var fileSize = line.Split(" ").Where(x => int.TryParse(x, out var canparse)).Select(x => int.Parse(x));

                    if (!fileSize.Any())
                        continue;

                    CurrentNode.FileDirSize += fileSize.First();
                }
            }
        }

        private static void CalcDirectorySizes(Node directory)
        {
            foreach(var node in directory.Children)
            {
                if (node.TotalDirSize < 100000)
                    LargeDirectories.Add(node.TotalDirSize);

                AllDirectorySizes.Add(node.TotalDirSize);
                CalcDirectorySizes(node);
            }
        }

        private static long GetDirectorySizeToDelete()
        {
            return AllDirectorySizes.Where(x => x > (30000000 - (70000000 - Directory.TotalDirSize))).OrderBy(x => x).First();
        }
    }
}