namespace No._4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<List<int>> elfSections = new List<List<int>>();
            int commonSectionCount = 0;
            int completeOverlap = 0;

            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                foreach (var elf in line.Split(','))
                {
                    var sections = new List<int>();
                    var startSection = int.Parse(elf.Split("-")[0]);
                    var endSection = int.Parse(elf.Split("-")[1]);

                    while (startSection != endSection)
                    {
                        sections.Add(startSection);
                        startSection++;
                    }

                    sections.Add(endSection);
                    elfSections.Add(sections);
                }

                var commonSections = elfSections[0].Intersect(elfSections[1]);
                
                if (commonSections.Count() > 0)
                {
                    completeOverlap++;
                }

                if (commonSections.SequenceEqual(elfSections[0]) || commonSections.SequenceEqual(elfSections[1]))
                {
                    commonSectionCount++;
                }

                elfSections.Clear();
            }

            Console.WriteLine($"Amount of common sections: {commonSectionCount}");
            Console.WriteLine($"Amount of complete overlap: {completeOverlap}");
            Console.ReadLine();
        }
    }
}