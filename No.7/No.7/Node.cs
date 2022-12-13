namespace No._7
{
    public class Node
    {
        public Node(Node previousNode)
        {
            PreviousNode = previousNode;
            Children = new List<Node>();
        }

        public Node PreviousNode { get; set; }

        public List<Node> Children { get; set; }

        public long FileDirSize { get; set; }

        public long TotalDirSize
        {
            get
            {
                var totalDirSize = FileDirSize;
                foreach (var node in Children)
                {
                    totalDirSize += node.TotalDirSize;
                }

                return totalDirSize;
            }
        }

        public string DirName { get; set; }
    }
}
