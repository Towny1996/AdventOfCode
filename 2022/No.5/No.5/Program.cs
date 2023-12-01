namespace No._5
{
    internal class Program
    {
        private static List<string> _startingStackLines = new List<string>();
        private static List<string> _instructionLines = new List<string>();
        private static List<Stack<string>> _crateStack = new List<Stack<string>>();

        static void Main(string[] args)
        {
            OrganiseStackAndInstructions();
            PopulateStartingStacks();
            MoveContainers();

            foreach(var stack in _crateStack)
            {
                Console.WriteLine(stack.First());
            }

            Console.ReadLine();
        }

        private static void OrganiseStackAndInstructions()
        {
            bool switchContext = false;
            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                if (string.IsNullOrEmpty(line))
                {
                    switchContext = true;
                    continue;
                }

                if (switchContext)
                {
                    _instructionLines.Add(line);
                }
                else
                {
                    _startingStackLines.Add(line);
                }
            }

            _startingStackLines.RemoveAt(_startingStackLines.Count - 1);
        }

        private static void PopulateStartingStacks()
        {
            foreach (var line in _startingStackLines)
            {
                var crates = line.Split(" ");
                var stack = 0;

                for (var i = 0; i < crates.Length; i++)
                {
                    if (_crateStack.ElementAtOrDefault(stack) == null)
                    {
                        _crateStack.Add(new Stack<string>());
                    }

                    if (string.IsNullOrEmpty(crates[i]))
                    {
                        i += 3;
                    } else
                    {
                        _crateStack[stack].Push(crates[i]);
                    }

                    stack++;
                }
            }

            for (var i = 0; i < _crateStack.Count; i++)
            {
                _crateStack[i] = new Stack<string>(_crateStack[i]);
            }
        }

        private static void MoveContainers()
        {
            foreach (var instruction in _instructionLines)
            {
                List<int> commands = instruction.Split(" ").Where(x => int.TryParse(x, out var success)).Select(x => int.Parse(x)).ToList();
                List<string> movingCrates = new List<string>();

                for (var i = 0; i < commands[0]; i++)
                {
                    movingCrates.Add(_crateStack[commands[1] - 1].Pop());
                }

                movingCrates.Reverse();

                foreach (var crate in movingCrates)
                {
                    _crateStack[commands[2] - 1].Push(crate);
                }
            }
        }
    }
}
