
namespace No._8
{
    internal class Program
    {
        private static int[,] Forest;

        private delegate int Direction(int x);

        private static int Add(int x) => x + 1;

        private static int Subtract(int x) => x - 1;

        static void Main(string[] args)
        {
            PopulateForest();
            Console.WriteLine($"Highest Tree Score: {CalcTreeVisibility()}");

            Console.ReadLine();
        }

        private static void PopulateForest()
        {
            var inputFile = File.ReadAllLines("Input.txt");
            Forest = new int[inputFile.Length, inputFile[0].Length];

            for (var l = 0; l < inputFile.Length; l++)
            {
                var line = inputFile[l];

                for (var h = 0; h < line.Length; h++)
                {
                    Forest[l, h] = int.Parse(line[h].ToString());
                }
            }
        }

        private static int CalcTreeVisibility()
        {
            List<int> treeScores = new List<int>();

            for (int y = 0; y < Forest.GetLength(0); y++)
            {
                for (int x = 0; x < Forest.GetLength(1); x++)
                {
                    var treeScoreXSub = CheckXSurroundingTrees(x - 1, 0, y, Forest[x, y], Subtract);
                    var treeScoreXAdd = CheckXSurroundingTrees(x + 1, (Forest.GetLength(0) - 1), y, Forest[x, y], Add);

                    var treeScoreYSub = CheckYSurroundingTrees(y - 1, 0, x, Forest[x, y], Subtract);
                    var treeScoreYAdd = CheckYSurroundingTrees(y + 1, (Forest.GetLength(1) - 1), x, Forest[x, y], Add);

                    treeScores.Add(treeScoreXSub * treeScoreXAdd * treeScoreYSub * treeScoreYAdd);
                }
            }

            return treeScores.MaxBy(x => x);
        }

        private static int CheckXSurroundingTrees(int starting, int ending, int y, int treeHeight, Direction direction)
        {
            int treeView = 0;
            
            while (direction == Subtract ? starting >= ending : starting <= ending) 
            {
                treeView++;

                if (Forest[starting, y] >= treeHeight)
                {
                    break;
                }

                starting = direction(starting);
            }

            return treeView;
        }

        private static int CheckYSurroundingTrees(int starting, int ending, int x, int treeHeight, Direction direction)
        {
            int treeView = 0;

            while (direction == Subtract ? starting >= ending : starting <= ending)
            {
                treeView++;

                if (Forest[x, starting] >= treeHeight)
                {
                    break;
                }

                starting = direction(starting);
            }

            return treeView;
        }
    }
}