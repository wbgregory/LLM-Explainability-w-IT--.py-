# LLM Explainability using Interaction Testing

## Purpose
The software within this repository has the ability to generate a candidate array (composed of synonym based sentences) given a sentence and validate it against a locating and covering array verifier, doing so until it generates an array that validates both verifier's requirements. After creating a valid locating/covering array, this software is then able to feed the sentence queries within the array into a LLM, at which point it stores the boolean response of the LLM and determines the accuracy and error points of the array (the synonyms that cause the most issues/inaccuracy). A draft portion has been added that factors in a dataset of possible sentence queries to be arrayed, but due to time constraints this portion has not been fully implemented yet (the response timing is time consuming when iterated over multiple times). 

## Functionality
To allow the software within this repository to function correctly, first download all files and store them within the same repository. Navigate to the synonym_generator file and run the ipynb in order from top-down, installing all necessary portions as they are presented in the ipynb file. After reaching the backup/stored code portion, navigate to the databricks_dolly file and begin, once again, going from the top-down, installing all necessary portions as they are presented in the ipynb file. You may need to update pip or be presented with an error in downloads, such as transformers. If this occurs, use pip to then install the individual transformers portion (though this should not occur). Test the functionality of the LLM using the coding portion below imports with the generate_text[] and print() statements. After validating the functionality of the LLM, proceed with the same top-down code approach, running each coding portion as it appears until you reach the "install datasets" portion. This coding block can be used, but a few changes must be made in order to have the sentences generate their own arrays and then have those be provided to the LLM for an output - this change is not difficult, but it will be very time consuming based on the number of sentences you intend to use. 