namespace No._6
{
    internal class Program
    {
        private static Queue<char> marker = new Queue<char>();

        static void Main(string[] args)
        {
            var line = File.ReadAllText("Input.txt");

            for (var i = 0; i < line.Length; i++)
            {
                marker.Enqueue(line[i]);

                if (marker.Count == 14 && marker.Distinct().Count() == 14)
                {
                    Console.WriteLine(i + 1);
                    break;
                } 
                else if (marker.Count == 14 && marker.Distinct().Count() != 14)
                {
                    marker.Dequeue();
                }
            }

            Console.ReadLine();
        }
    }
}