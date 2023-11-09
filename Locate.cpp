#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(la_analysis, m)
{
    m.doc() = "error analysis plugin"; // optional module docstring

    m.def("LA Analysis", $./ Search[LocatingArray.tsv]([FactorData.tsv]) analysis[ResponsesDirectory][response_column][1 / 0 - perform log on responses][nTerms][nModels][nNewModels], "A function that adds two numbers");
}

// two options - one, execute within locate.cpp and return the output within the ipynb file, or two, bring ipynb files to
// the cpp file and operate from there

// input the locating array file for each sentence
// iterate over the three sentences used

$./ Search[LocatingArray.tsv]([FactorData.tsv]) analysis[ResponsesDirectory][response_column][1 / 0 - perform log on responses][nTerms][nModels][nNewModels]
