using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

namespace No._9
{
    public class Part_2
    {
        private static string[,] Map;
        private static List<int[]> VisitedTiles;

        private static List<int[]> KnotLocs = new List<int[]>();

        public Part_2()
        {
            VisitedTiles = new List<int[]>();
            PopulateStartingKnotLocations();

            LogMap();
            MoveRope();

            Console.WriteLine();
            Console.WriteLine($"Unique Visited Tiles: {VisitedTiles.Count()}");
            Console.ReadLine();
        }

        private static void PopulateStartingKnotLocations()
        {
            for (int i = 0; i <= 10; i++)
            {
                var knotLoc = new int[2];
                knotLoc[0] = 16;
                knotLoc[1] = 12;

                KnotLocs.Add(knotLoc);
            }
        }
        
        private static void MoveRope()
        {
            foreach (var line in File.ReadAllLines("Input.txt"))
            {
                var direction = line.Split(' ')[0];
                int moves = int.Parse(line.Split(" ")[1]);

                for (int i = 0; i < moves; i++)
                {
                    switch (direction)
                    {
                        case "U":
                            KnotLocs[0][0] -= 1;
                            break;
                        case "D":
                            KnotLocs[0][0] += 1;
                            break;
                        case "R":
                            KnotLocs[0][1] += 1;
                            break;
                        case "L":
                            KnotLocs[0][1] -= 1;
                            break;
                    }

                    LogMap();
                    CheckAndMoveTails();
                }
            }
        }

        private static void CheckAndMoveTails()
        {
            for (var i = 1; i < KnotLocs.Count; i++)
            {
                if ((KnotLocs[i - 1][0] > KnotLocs[i][0] + 1) || (KnotLocs[i - 1][0] < KnotLocs[i][0] - 1))
                {
                    if (KnotLocs[i - 1][0] > KnotLocs[i][0])
                    {
                        if (KnotLocs[i - 1][1] < KnotLocs[i][1])
                        {
                            KnotLocs[i][1] -= 1;
                        }
                        else if (KnotLocs[i - 1][1] > KnotLocs[i][1])
                        {
                            KnotLocs[i][1] += 1;
                        }

                        KnotLocs[i][0] += 1;
                    }
                    else
                    {
                        if (KnotLocs[i - 1][1] < KnotLocs[i][1])
                        {
                            KnotLocs[i][1] -= 1;
                        }
                        else if (KnotLocs[i - 1][1] > KnotLocs[i][1])
                        {
                            KnotLocs[i][1] += 1;
                        }

                        KnotLocs[i][0] -= 1;
                    }

                    if (i == KnotLocs.Count)
                    {
                        AddVisitedTile(KnotLocs[i][0], KnotLocs[i][1]);
                    }
                }

                if ((KnotLocs[i - 1][1] > KnotLocs[i][1] + 1) || (KnotLocs[i - 1][1] < KnotLocs[i][1] - 1))
                {
                    if (KnotLocs[i - 1][1] > KnotLocs[i][1])
                    {
                        if (KnotLocs[i - 1][0] < KnotLocs[i][0])
                        {
                            KnotLocs[i][0] -= 1;
                        }
                        else if (KnotLocs[i - 1][0] > KnotLocs[i][0])
                        {
                            KnotLocs[i][0] += 1;
                        }

                        KnotLocs[i][1] += 1;
                    }
                    else
                    {
                        if (KnotLocs[i - 1][0] < KnotLocs[i][0])
                        {
                            KnotLocs[i][0] -= 1;
                        }
                        else if (KnotLocs[i - 1][0] > KnotLocs[i][0])
                        {
                            KnotLocs[i][0] += 1;
                        }

                        KnotLocs[i][1] -= 1;
                    }


                    if (i == KnotLocs.Count)
                    {
                        AddVisitedTile(KnotLocs[i][0], KnotLocs[i][1]);
                    }
                }

                LogMap();
            }
        }

        private static void AddVisitedTile(int x, int y)
        {
            var visitedTile = new[] { x, y };
            if (!VisitedTiles.Any(x => x.SequenceEqual(visitedTile)))
            {
                VisitedTiles.Add(new[] { x, y });
            }
        }

        private static void LogMap()
        {
            Thread.Sleep(50);
            Console.SetCursorPosition(0, 0);
            Map = new string[21, 26];

            for (var x = 0; x < Map.GetLength(0); x++)
            {
                Console.WriteLine();
                for (var y = 0; y < Map.GetLength(1); y++)
                {
                    if (KnotLocs.Any(z => z[0] == x && z[1] == y))
                    {
                        Map[x, y] = " O ";
                    }
                    else
                    {
                        Map[x, y] = $" x ";
                    }

                    Console.Write(Map[x, y]);
                }
            }
        }
    }
}
