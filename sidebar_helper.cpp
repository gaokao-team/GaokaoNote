#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>

using std::endl;
using std::ofstream;
using std::ifstream;
using std::string;
using std::filesystem::directory_iterator;

int main() 
{
    string path = std::filesystem::current_path().generic_string();
    ofstream output;
    output.open(path + "/_sidebar.md");
    for (const auto & sub : directory_iterator(path))
    {
      if (!sub.is_directory()) continue;
      if (sub.path().filename() == ".git" || sub.path().filename() == ".vscode") continue;
      output << "  - " << sub.path().filename().generic_string() << endl;
      for (const auto &file : directory_iterator(sub.path())) 
      {
          if(file.path().extension() == ".md")
          {
              ifstream reader;
              reader.open(file.path());
              string now;
              do { reader >> now; }while(now != "#");
              getline(reader,now);
              while(now.back() == ' ') now.pop_back();
              while(now.front() == ' ') now.erase(now.begin());
              //now is the title of the file
              output << "    - [" << now << "](/" << sub.path().filename().generic_string()
                     << '/' << file.path().filename().generic_string() << ')' << endl;
              reader.close();
          }
      }
    }
    return 0;
}