let adjList = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: ["a"],
  f: [],
};

var visited = [];
const bfs_queue = (graph, source) => {
  var queue = [source];
  visited.push(source);
  while (queue.length > 0) {
    let current = queue.shift();
    console.log(current);

    graph[current].forEach((neighbor) => {
      if (!visited.includes(neighbor)) {
        visited.push(neighbor);
        queue.push(neighbor);
      }
    });
  }
};
const dfs_stack = (graph, source) => {
  var stack = [source];
  while (stack.length > 0) {
    let current = stack.pop();
    console.log(current);

    graph[current].forEach((neighbor) => {
      stack.push(neighbor);
    });
  }
};
const dfs_recursion = (graph, source) => {
  console.log(source);
  graph[source].forEach((neighbor) => {
    dfs_recursion(graph, neighbor);
  });
};

var flag = false;
const hasPath_dfs_stack = (graph, src, dst) => {
  var stack = [src];
  visited.push(src);
  while (stack.length > 0) {
    let current = stack.pop();
    if (current == dst) {
      flag = true;
      return;
    }
    graph[current].forEach((neighbor) => {
      if (!visited.includes(neighbor)) {
        visited.push(neighbor);
        stack.push(neighbor);
      }
    });
  }
};
const hasPath_dfs_recursion = (graph, src, dst) => {
  if (src == dst) {
    flag = true;
    return;
  }
  visited.push(src);
  graph[src].forEach((neighbor) => {
    if (!visited.includes(neighbor)) {
      visited.push(neighbor);

      hasPath_dfs_recursion(graph, neighbor, dst);
    }
  });
};
const hasPath_bfs = (graph, src, dst) => {
  var queue = [src];
  visited.push(src);
  while (queue.length > 0) {
    let current = queue.shift();
  }
};

const edges = [
  ["i", "j"],
  ["k", "i"],
  ["m", "k"],
  ["k", "l"],
  ["o", "n"],
];

const dfs_hasPath_recursion = (graph, nodeA, nodeB) => {
  visited.push(nodeA);
  if (nodeA == nodeB) {
    flag = true;
    return;
  }

  graph[nodeA].forEach((neighbor) => {
    if (!visited.includes(neighbor)) {
      dfs_hasPath_recursion(graph, neighbor, nodeB);
    }
  });
};
const undirectedPath = (edges, nodeA, nodeB) => {
  var Created_adjList = [];
  edges.forEach((edge) => {
    const [src, dst] = edge;
    if (!(src in Created_adjList)) Created_adjList[src] = [];
    if (!(dst in Created_adjList)) Created_adjList[dst] = [];
    Created_adjList[src].push(dst);
    Created_adjList[dst].push(src);
  });
  console.log(Created_adjList);
  dfs_hasPath_recursion(Created_adjList, nodeA, nodeB);
  console.log(flag);
  console.log(visited);
};

// undirectedPath(edges, "j", "m"); // -> true

const connectedComponentsCount_BFS = (graph) => {
  var count = 0;
  for (var [node, value] of Object.entries(graph)) {
    node = parseInt(node);
    if (!visited.includes(node)) {
      console.log(visited);
      count += 1;
      var queue = [node];
      visited.push(node);
      while (queue.length > 0) {
        let current = queue.shift();
        visited.push[current];
        graph[current].forEach((neighbor) => {
          if (!visited.includes(neighbor)) {
            visited.push(neighbor);
            queue.push(neighbor);
          }
        });
      }
    }
  }
  return count;
};
const connectedComponentsCount_Recursion_DFS = (graph) => {
  let count = 0;
  for (var [node, value] of Object.entries(graph)) {
    node = parseInt(node);
    if (!visited.includes(node)) {
      count += 1;
      explore(graph, node);
    }
  }
  return count;
};
const explore = (graph, src) => {
  if (!visited.includes(src)) {
    visited.push(src);
    graph[src].forEach((neighbor) => {
      explore(graph, neighbor);
    });
  }
};

// console.log(
//   connectedComponentsCount_Recursion_DFS({
//     0: [4, 7],
//     1: [],
//     2: [],
//     3: [6],
//     4: [0],
//     6: [3],
//     7: [0],
//     8: [],
//   })
// );

const largestComponent = (graph) => {
  var max = 0;
  for (var [node, value] of Object.entries(graph)) {
    var count = exploreSize_BFS(graph, node);

    if (count > max) max = count;
    //console.log(count);
  }
  return max;
};

const exploreSize_recursion_dfs = (graph, src) => {};

const exploreSize_BFS = (graph, src) => {
  if (!visited.includes(src)) {
    var count = 1;
    const queue = [src];
    while (queue.length > 0) {
      console.log(queue);
      var current = queue.shift();

      visited.push(current);
      graph[current].forEach((neighbor) => {
        if (!visited.includes(neighbor)) {
          queue.push(neighbor);
          count += 1;
        }
      });
    }
    return count;
  }

  return 0;
};

// console.log(
//   largestComponent({
//     0: ["4", "7"],
//     1: [],
//     2: [],
//     3: ["6"],
//     4: ["0"],
//     6: ["3"],
//     7: ["0"],
//     8: [],
//   })
// );
const edges2 = [
  ["m", "n"],
  ["n", "o"],
  ["o", "p"],
  ["p", "q"],
  ["t", "o"],
  ["r", "q"],
  ["r", "s"],
];

const convertEdgesToAdjList = (edges) => {
  const adjList = {};
  for (const [src, dst] of edges) {
    if (!(src in adjList)) adjList[src] = [];
    if (!(dst in adjList)) adjList[dst] = [];
    adjList[src].push(dst);
    adjList[dst].push(src);
  }
  return adjList;
};

const shortestPath = (edges, nodeA, nodeB) => {
  const graph = convertEdgesToAdjList(edges);
  const queue = [[nodeA, 0]];
  visited.push(nodeA);
  while (queue.length > 0) {
    let current = queue.shift();
    visited.push(current[0]);
    if (current[0] == nodeB) {
      return current[1];
    }
    graph[current[0]].forEach((neighbor) => {
      if (!visited.includes(neighbor)) {
        queue.push([neighbor, current[1] + 1]);
      }
    });
  }
  return -1;
};

// console.log(shortestPath(edges2, "m", "s"));

const explore_DFS_Recursion = (grid, i, j) => {
  if (i == grid.length) i = 0;
  if (i < 0) i = grid.length - 1;
  var gridRow = grid[i];
  // console.log("I: " + i);
  // console.log(gridRow);
  if (j == gridRow.length) j = 0;
  if (j < 0) j = gridRow.length - 1;
  if (grid[i][j] == "W") return;

  // console.log(visited);
  if (!visited.includes(i + " " + j)) {
    visited.push(i + " " + j);
    // console.log([i, j]);
    explore_DFS_Recursion(grid, i + 1, j);
    explore_DFS_Recursion(grid, i - 1, j);
    explore_DFS_Recursion(grid, i, j + 1);
    explore_DFS_Recursion(grid, i, j - 1);
  } else {
    // console.log("GET ME FKN OUT PLEASE");
    return;
  }
};

const islandCount = (grid) => {
  var count = 0;
  for (var i = 0; i < grid.length; i++) {
    for (var j = 0; j < grid[i].length; j++) {
      if (!visited.includes(i + " " + j) && grid[i][j] == "L") {
        count += 1;
        // console.log("iterate: " + i + " " + j);
        explore_DFS_Recursion(grid, i, j);
      }
    }
  }
  console.log(count);
};
// islandCount(grid);
var c = 0;
const countThisIsland = (grid, i, j) => {
  console.log(c);
  if (i == grid.length) i = 0;
  if (i < 0) i = grid.length - 1;
  if (j == grid[i].length) j = 0;
  if (j < 0) j = grid[i].length - 1;
  if (grid[i][j] == "W" || visited.includes(i + "," + j)) return;
  c += 1;
  visited.push(i + "," + j);
  countThisIsland(grid, i + 1, j);
  countThisIsland(grid, i - 1, j);
  countThisIsland(grid, i, j + 1);
  countThisIsland(grid, i, j - 1);
  return c;
};

const minimumIsland = (grid) => {
  var min = grid.length * grid[0].length + 1;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == "L" && !visited.includes(i + "," + j)) {
        c = 0;
        var count = countThisIsland(grid, i, j);
        console.log("Iterate: " + i + " " + j);
        if (count < min) {
          min = count;
        }
      }
    }
  }
  console.log(min);
  console.log(visited);
};
const grid = [
  ["W", "W"],
  ["L", "L"],
  ["W", "W"],
  ["W", "L"],
];

minimumIsland(grid);
