#include <bits/stdc++.h>

using namespace std;

#if defined(__linux__) // Ou #if __linux__
const string limpar = "clear";
const string apagar = "rm x.out";
const string barra = "/";
const string diff = "diff";
#elif _WIN32
const string limpar = "cls";
const string apagar = "del x.out";
const string barra = "\\";
const string diff = "FC";
#endif

int main(void)
{
    vector<pair<string, int>> returns;
    int passed = 0, failed = 0;
    string file_name, case_test_in_folder, case_test_out_folder;
    int num_off_tests;

    cout << "Insira o nome do arquivo com extenção: (Não utilize espaço, caracteres especiais ou assentuação no nome do arquivo)" << endl;

    cin >> file_name;

    cout << "Insira o nome do diretorio com os casos de testes de entrada. (Mesmas regras acima)" << endl;

    cin >> case_test_in_folder;

    cout << "Insira o nome do diretorio com os casos de testes de saida. (Mesmas regras acima)" << endl;

    cin >> case_test_out_folder;

    cout << "Insira quantidade de casos de testes:" << endl;

    cin >> num_off_tests;

    system(limpar.c_str());
    system("mkdir -p sfout");

    for (int i = 1; i <= num_off_tests; i++)
    {
        string c = "";
        if (i < 10)
        {
            c = "0";
        }
        string temp = "python " + file_name + " < " + case_test_in_folder + barra + c + to_string(i) + ".in > x.out";

        system(temp.c_str());

        temp = diff + " x.out " + case_test_out_folder + barra + c + to_string(i) + ".out > sfout" + barra + "k" + to_string(i) + ".txt";

        system(temp.c_str());

        FILE *file;

        temp = "sfout" + barra + "k" + to_string(i) + ".txt";

        file = fopen(temp.c_str(), "r");

        if (file == NULL)
        {
            cout << "Erro ao abrir arquivo" << endl;
        }

        char sts[201] = "";
        string res = "";

        while (feof(file) == 0)
        {
            fgets(sts, 200, file);
            res += sts;
        }

        if (res == "")
        {
            passed++;
        }
        else
        {
            failed++;
            returns.push_back({res, i});
        }
    }

    system(apagar.c_str());

    cout << endl
         << "------------------------------------------------------------------------------------" << endl
         << "O programa acertou: " << passed << " Casos de testes.\nE errou: " << failed << endl
         << endl;

    for (pair<string, int> i : returns)
    {
        cout << "Teste: " << i.second << " Falho.\n"
             << "Retorno: " << i.first << endl
             << endl;
    }

    return 0;
}