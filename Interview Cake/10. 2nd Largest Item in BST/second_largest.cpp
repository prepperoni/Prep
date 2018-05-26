#include <iostream>
#include <memory>

// C++11 lest unit testing framework
#include "lest.hpp"

using namespace std;

class BinaryTreeNode
{
public:
    int value_;
    BinaryTreeNode* left_;
    BinaryTreeNode* right_;

    BinaryTreeNode(int value) :
        value_(value),
        left_(nullptr),
        right_(nullptr)
    {
    }

    ~BinaryTreeNode()
    {
        delete left_;
        delete right_;
    }

    BinaryTreeNode* insertLeft(int value)
    {
        this->left_ = new BinaryTreeNode(value);
        return this->left_;
    }

    BinaryTreeNode* insertRight(int value)
    {
        this->right_ = new BinaryTreeNode(value);
        return this->right_;
    }
};

vector<BinaryTreeNode*> goRight(BinaryTreeNode* node) {
    auto preNode = new BinaryTreeNode(0);
    preNode->right_ = node;
    
    while (node->right_ != nullptr) {
        node = node->right_;
        preNode = preNode->right_;
    }

    return {preNode, node};
}

int findSecondLargest(BinaryTreeNode* rootNode)
{
    // find the second largest item in the binary search tree
    vector<BinaryTreeNode*> rightNodes = goRight(rootNode);
    
    if (rightNodes[1] != rootNode and rightNodes[1]->left_ == nullptr) {
        return rightNodes[0]->value_;
    }

    return goRight(rightNodes[1]->left_)[1]->value_;
}

// tests

const lest::test tests[] = {
    CASE("Full tree") {
        auto root = make_shared<BinaryTreeNode>(50);
        root->insertLeft(30)->insertLeft(10);
        root->insertRight(70)->insertRight(80);
        root->left_->insertRight(40);
        root->right_->insertLeft(60);
        EXPECT(findSecondLargest(root.get()) == 70);
    },
    CASE("Largest has a left child") {
        auto root = make_unique<BinaryTreeNode>(50);
        root->insertLeft(30)->insertLeft(10);
        root->insertRight(70)->insertLeft(60);
        root->left_->insertRight(40);
        EXPECT(findSecondLargest(root.get()) == 60);
    },
    CASE("Largest has a left subtree") {
        auto root = make_unique<BinaryTreeNode>(50);
        root->insertLeft(30)->insertLeft(10);
        root->left_->insertRight(40);
        root->insertRight(70)->insertLeft(60)->insertLeft(55)->insertRight(58);
        root->right_->left_->insertRight(65);
        EXPECT(findSecondLargest(root.get()) == 65);
    },
    CASE("Second largest is root node") {
        auto root = make_unique<BinaryTreeNode>(50);
        root->insertLeft(30)->insertLeft(10);
        root->insertRight(70);
        root->left_->insertRight(40);
        EXPECT(findSecondLargest(root.get()) == 50);
    },
    CASE("Descending linked list") {
        auto root = make_unique<BinaryTreeNode>(50);
        root->insertLeft(40)->insertLeft(30)->insertLeft(20)->insertLeft(10);
        EXPECT(findSecondLargest(root.get()) == 40);
    },
    CASE("Ascending linked list") {
        auto root = make_unique<BinaryTreeNode>(50);
        root->insertRight(60)->insertRight(70)->insertRight(80);
        EXPECT(findSecondLargest(root.get()) == 70);
    },
    CASE("Exception when tree has one node") {
        auto root = make_unique<BinaryTreeNode>(50);
        EXPECT_THROWS(findSecondLargest(root.get()));
    },
    CASE("Exception when tree is empty") {
        EXPECT_THROWS(findSecondLargest(nullptr));
    },
};

int main(int argc, char** argv)
{
    return lest::run(tests, argc, argv);
}