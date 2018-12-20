# CodeLanguage
A project loading data from the CSV file, predicting the programing language used to write each part of the code.

A SVM model is being being after loading the data from the .csv file. Data need to be structured in a "language,proj_id,file_id,file_body" manner for provided class to load it.
The program builds a huge dictionary with all words and special characters in provided code. It is being used for building feature matrix. The PCA algorithm is used for sake of extacting the important features. Then, SVM model is being trained using those features.
The classification process is undertaken using the batch of codes beloning to a given project. Then, the label for all of the files in project is yielded based for most frequent label present in vector of all labels for the project file.
The project will work only for the following programming languages: {'Swift', 'C++', 'Kotlin', 'Scala', 'Java', 'Mathematica', 'C', 'Python', 'Haskell', 'Ruby', 'Fortran', 'MATLAB', 'Perl', 'Go', 'R', 'JavaScript', 'PHP', 'Rust', 'Julia'}
To detect another language, it needs to be added to the Languages enum located in the data_management.py file. 
