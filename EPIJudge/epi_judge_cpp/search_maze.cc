#include <istream>
#include <string>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/test_utils_serialization_traits.h"
#include "test_framework/timed_executor.h"

using std::vector;

typedef enum { kWhite, kBlack } Color;

struct Coordinate {
  bool operator==(const Coordinate& that) const {
    return x == that.x && y == that.y;
  }

  int x, y;
};

bool traverse(vector<vector<Color>> &maze, vector<Coordinate> &path, const Coordinate cur, const Coordinate& e) {
	if (cur.x < 0 || cur.x >= maze.size() || cur.y < 0 || cur.y >= maze[0].size() || maze[cur.x][cur.y] == kBlack) {
		return false;
	}
 
  if (cur == e) {
    path.emplace_back(cur);
    return true;
  }

  maze[cur.x][cur.y] = kBlack;
  path.emplace_back(cur);
  vector<vector<int>> directions {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
  bool status = false;

  for (auto &d : directions) {
	  if (traverse(maze, path, Coordinate{ cur.x + d[0], cur.y + d[1] }, e)) {
		  return true;
	  }
  }

  path.pop_back();
  return status;
}

vector<Coordinate> SearchMaze(vector<vector<Color>> maze, const Coordinate& s, const Coordinate& e) {
  vector<Coordinate> path;
  traverse(maze, path, s, e);
  return path;
}

template <>
struct SerializationTraits<Color> : SerializationTraits<int> {
  using serialization_type = Color;

  static serialization_type Parse(const std::string& str) {
    return static_cast<serialization_type>(
        SerializationTraits<int>::Parse(str));
  }

  static serialization_type JsonParse(std::istream& in) {
    return static_cast<serialization_type>(
        SerializationTraits<int>::JsonParse(in));
  }
};

template <>
struct SerializationTraits<Coordinate> : UserSerTraits<Coordinate, int, int> {};

bool PathElementIsFeasible(const vector<vector<Color>>& maze,
                           const Coordinate& prev, const Coordinate& cur) {
  if (!(0 <= cur.x && cur.x < maze.size() && 0 <= cur.y &&
        cur.y < maze[cur.x].size() && maze[cur.x][cur.y] == kWhite)) {
    return false;
  }
  return cur == Coordinate{prev.x + 1, prev.y} ||
         cur == Coordinate{prev.x - 1, prev.y} ||
         cur == Coordinate{prev.x, prev.y + 1} ||
         cur == Coordinate{prev.x, prev.y - 1};
}

bool SearchMazeWrapper(TimedExecutor& executor,
                       const vector<vector<Color>>& maze, const Coordinate& s,
                       const Coordinate& e) {
  vector<vector<Color>> copy = maze;

  auto path = executor.Run([&] { return SearchMaze(copy, s, e); });

  if (path.empty()) {
    return s == e;
  }

  if (!(path.front() == s) || !(path.back() == e)) {
    throw TestFailure("Path doesn't lay between start and end points");
  }

  for (size_t i = 1; i < path.size(); i++) {
    if (!PathElementIsFeasible(maze, path[i - 1], path[i])) {
      throw TestFailure("Path contains invalid segments");
    }
  }

  return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "maze", "s", "e"};
  return GenericTestMain(args, "search_maze.tsv", &SearchMazeWrapper,
                         DefaultComparator{}, param_names);
}
