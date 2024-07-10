#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

// const unordered_set<string> commentSigns = {"#", "//", "/*", "*/"};


void getTotalCharsInSolution(const string& InputPath, const string& OutputPath) {
    fstream fileInput(InputPath);
    if (!fileInput.is_open()) {
        throw runtime_error("file is not open");
    }
    string tempString;
    size_t totalCnt = 0;
    while (getline(fileInput, tempString)) {
        int cntInRow = 0;
        for (const auto & elem : tempString) {
            if (elem == '#') {
                break;
            } else if (elem == ' ' || elem == '\n' || elem == '\t') {
                continue;
            } else {
                cntInRow++;
            }
        }
        totalCnt += cntInRow;
    }
    fstream fileOutput(OutputPath, fstream::app);
    fileOutput << "Task name: " << InputPath << '\n';
    fileOutput << "Total chars count: " << totalCnt << '\n';
    fileOutput.close();
    fileInput.close();

}

const int CNT_TASKS = 20;
const string DEEP_SEEK_CODE_FILES_SOLUTIONS = "deepseekcode/";
const string USERS_FILES_SOLUTIONS = "usersolution/";
const string GIGACODE_FILES_SOLUTION = "gigacode/";

int main() {
    const vector<string> file_names = {"1. Two Sum (Easy)",
                                       "2. Add Two Numbers (Medium)",
                                       "3. Longest Substring Without Repeating Characters (Medium)",
                                       "4. Median of Two Sorted Arrays (Hard)",
                                       "5. Longest Palindromic Substring (Medium)",
                                       "6. Zigzag Conversion (Medium)",
                                       "7. Reverse Integer (Medium)",
                                       "8. String to Integer (atoi) (Medium)",
                                       "9. Palindrome Number (Easy)",
                                       "10. Regular Expression Matching (Hard)",
                                       "11. Container With Most Water (Medium)",
                                       "12. Integer to Roman (Medium)",
                                       "13. Roman to Integer (Easy)",
                                       "14. Longest Common Prefix (Easy)",
                                       "15. 3Sum (Medium)",
                                       "16. 3Sum Closest (Medium)",
                                       "17. Letter Combinations of a Phone Number (Medium)",
                                       "18. 4Sum (Medium)",
                                       "19. Remove Nth Node From End of List (Medium)",
                                       "20. Valid Parentheses (Easy)"};

    const string deepseekcodePathOutput = "results_deepseekcode.txt";
    const string userPathOutput = "result_user.txt";
    const string gigaCodeOutput = "results_GigaCode.txt";

    for (int i = 0; i < CNT_TASKS; ++i)
        getTotalCharsInSolution(DEEP_SEEK_CODE_FILES_SOLUTIONS + file_names[i], DEEP_SEEK_CODE_FILES_SOLUTIONS + deepseekcodePathOutput);

    for (int i = 0; i < CNT_TASKS; ++i)
        getTotalCharsInSolution(USERS_FILES_SOLUTIONS + file_names[i], USERS_FILES_SOLUTIONS + userPathOutput);

    for (int i = 0; i < CNT_TASKS; ++i)
        getTotalCharsInSolution(GIGACODE_FILES_SOLUTION + file_names[i], GIGACODE_FILES_SOLUTION + gigaCodeOutput);

}

