#include <vector>
#include <unordered_map>
#include <list>
#include <utility>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/test_utils_serialization_traits.h"

using namespace std;

class LruCache {
 public:
  LruCache(size_t capacity) : cap(capacity) {}

  int Lookup(int isbn) {
    if (d.find(isbn) == d.end()) {
      return -1;
    }

    int price = d[isbn].first;
    q.erase(d[isbn].second);
    q.emplace_front(isbn);
    d[isbn] = {price, q.begin()};
    return price;
  }

  void Insert(int isbn, int price) {
    if (d.find(isbn) != d.end()) {
      Lookup(isbn);
      return;
    }

    if (d.size() == cap) {
      d.erase(q.back());
      q.pop_back();
    }

    q.emplace_front(isbn);
    d[isbn] = {price, q.begin()};
  }

  bool Erase(int isbn) {
    if (d.find(isbn) == d.end()) {
      return false;
    } else {
      q.erase(d[isbn].second);
      d.erase(isbn);
      return true;
    }
  }

 private:
  unordered_map<int, pair<int, list<int>::iterator>> d;
  list<int> q;
  int cap;
};

struct Op {
  std::string code;
  int arg1;
  int arg2;
};

template <>
struct SerializationTraits<Op> : UserSerTraits<Op, std::string, int, int> {};

void RunTest(const std::vector<Op>& commands) {
  if (commands.empty() || commands[0].code != "LruCache") {
    throw std::runtime_error("Expected LruCache as first command");
  }
  LruCache cache(commands[0].arg1);

  for (int i = 1; i < commands.size(); i++) {
    auto& cmd = commands[i];
    if (cmd.code == "lookup") {
      int result = cache.Lookup(cmd.arg1);
      if (result != cmd.arg2) {
        throw TestFailure("Lookup: expected " + std::to_string(cmd.arg2) +
                          ", got " + std::to_string(result));
      }
    } else if (cmd.code == "insert") {
      cache.Insert(cmd.arg1, cmd.arg2);
    } else if (cmd.code == "erase") {
      bool result = cache.Erase(cmd.arg1);
      if (result != cmd.arg2) {
        throw TestFailure("Erase: expected " + std::to_string(cmd.arg2) +
                          ", got " + std::to_string(result));
      }
    } else {
      throw std::runtime_error("Unexpected command " + cmd.code);
    }
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"commands"};
  return GenericTestMain(args, "lru_cache.tsv", &RunTest, DefaultComparator{},
                         param_names);
}
