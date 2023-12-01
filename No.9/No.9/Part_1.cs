using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace No._9
{
    public class Part_1
    {
        private static string[,] Map;
        private static List<int[]> VisitedTiles;

        private static int[] HeadLoc = new int[2];
        private static int[] TailLoc = new int[2];

        public Part_1()
        {
            HeadLoc[0] = TailLoc[0] = 4;
            HeadLoc[1] = TailLoc[1] = 0;
            VisitedTiles = new List<int[]> { new[] { TailLoc[0], TailLoc[1] } };

            LogMap();
            MoveRope();

            Console.WriteLine();
            Console.WriteLine($"Unique Visited Tiles: {VisitedTiles.Count()}");
            Console.ReadLine();
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
                            HeadLoc[0] -= 1;
                            break;
                        case "D":
                            HeadLoc[0] += 1;
                            break;
                        case "R":
                            HeadLoc[1] += 1;
                            break;
                        case "L":
                            HeadLoc[1] -= 1;
                            break;
                    }

                    LogMap();
                    CheckAndMoveTail();
                }
            }
        }

        private static void CheckAndMoveTail()
        {
            if ((HeadLoc[0] > TailLoc[0] + 1) || (HeadLoc[0] < TailLoc[0] - 1))
            {
                if (HeadLoc[0] > TailLoc[0])
                {
                    if (HeadLoc[1] < TailLoc[1])
                    {
                        TailLoc[1] -= 1;
                    }
                    else if (HeadLoc[1] > TailLoc[1])
                    {
                        TailLoc[1] += 1;
                    }

                    TailLoc[0] += 1;
                }
                else
                {
                    if (HeadLoc[1] < TailLoc[1])
                    {
                        TailLoc[1] -= 1;
                    }
                    else if (HeadLoc[1] > TailLoc[1])
                    {
                        TailLoc[1] += 1;
                    }

                    TailLoc[0] -= 1;
                }

                AddVisitedTile(TailLoc[0], TailLoc[1]);
            }

            if ((HeadLoc[1] > TailLoc[1] + 1) || (HeadLoc[1] < TailLoc[1] - 1))
            {
                if (HeadLoc[1] > TailLoc[1])
                {
                    if (HeadLoc[0] < TailLoc[0])
                    {
                        TailLoc[0] -= 1;
                    }
                    else if (HeadLoc[0] > TailLoc[0])
                    {
                        TailLoc[0] += 1;
                    }

                    TailLoc[1] += 1;
                }
                else
                {
                    if (HeadLoc[0] < TailLoc[0])
                    {
                        TailLoc[0] -= 1;
                    }
                    else if (HeadLoc[0] > TailLoc[0])
                    {
                        TailLoc[0] += 1;
                    }

                    TailLoc[1] -= 1;
                }

                AddVisitedTile(TailLoc[0], TailLoc[1]);
            }

            LogMap();
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
            Console.SetCursorPosition(0, 0);
            Map = new string[5, 6];

            for (var x = 0; x < Map.GetLength(0); x++)
            {
                Console.WriteLine();
                for (var y = 0; y < Map.GetLength(1); y++)
                {
                    if (HeadLoc[0] == x && HeadLoc[1] == y)
                    {
                        Map[x, y] = $" H ";
                    }
                    else if ((TailLoc[0] == x && TailLoc[1] == y) && (HeadLoc[0] != TailLoc[0] || HeadLoc[1] != TailLoc[1]))
                    {
                        Map[x, y] = $" T ";
                    }
                    else
                    {
                        //Map[x, y] = $" {x},{y} ";
                        Map[x, y] = $" x ";
                    }

                    Console.Write(Map[x, y]);
                }
            }
        }
    }
}
