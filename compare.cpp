#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

const int CNT_TASKS = 20;
const string PATH_TO_DEEPSEEKCODE_FILES = "deepseekcode/results_deepseekcode.txt";
const string PATH_TO_GIGA_CODE_FILES = "gigacode/results_GigaCode.txt";
const string PATH_TO_USER_FILES = "usersolution/result_user.txt";

class Chars_cnt {
public:
    int dsc;
    int gc;
    int user;
    Chars_cnt() = default;
    Chars_cnt(int dsc, int gc, int user) : dsc(dsc), gc(gc), user(user) {}
};

int getCntFromString(const std::string& s) {
    size_t pos = s.find(':');
    if (pos == std::string::npos) {
        return 0;
    }
    return std::stoi(s.substr(pos + 1));
}

vector<Chars_cnt> parseResults(const string& path_to_deepseekcode_files,
                               const string& path_to_gigacode_files,
                               const string& path_to_user_solutions_files)
{
    vector<Chars_cnt> res(CNT_TASKS);
    fstream dsc_file(path_to_deepseekcode_files);
    fstream gc_file(path_to_gigacode_files);
    fstream user_file(path_to_user_solutions_files);

    for (int i = 0; i < CNT_TASKS; ++i) {
        string files_name;
        string cnt_string_dsc;
        string cnt_string_gc;
        string cnt_string_user;
        getline(dsc_file, files_name);
        getline(dsc_file, cnt_string_dsc);
        getline(gc_file, files_name);
        getline(gc_file, cnt_string_gc);
        getline(user_file, files_name);
        getline(user_file, cnt_string_user);

        res[i] = {getCntFromString(cnt_string_dsc), getCntFromString(cnt_string_gc), getCntFromString(cnt_string_user)};
    }
    return res;
}

int main() {
    vector<Chars_cnt> compare = parseResults(PATH_TO_DEEPSEEKCODE_FILES, PATH_TO_GIGA_CODE_FILES, PATH_TO_USER_FILES);

    int score_dsc = 0;
    int score_gc = 0;
    int score_user = 0;
    for (auto & [d, g, u] : compare) {
        if (d < g && d < u) {
            score_dsc++;
        } else if (g < d && g < u) {
            score_gc++;
        } else if (u < d && u < g) {
            score_user++;
        }
    }

    double percent_dsc = score_dsc * 100 / 20;
    double percent_gc = score_gc * 100 / 20;
    double percent_user = score_user * 100 / 20;
    double some_equal = 100 - percent_dsc - percent_gc - percent_user;

    fstream compare_result("Compare result.txt");
    if (!compare_result.is_open()) {
        throw runtime_error("file is not open");
    } else {
        compare_result << "Percent of deepseekcode win: " << percent_dsc << "%\n";
        compare_result << "Percent of gigacode win: " << percent_gc << "%\n";
        compare_result << "Percent of user win: " << percent_user << "%\n";
    }

    return 0;
}
