## Train the model with Allennlp 

######`cd ./my_library/../`  

######`run`: allennlp train tests/academic_paper_classifier.json -s tests/output_dir  --include-package my_library

#### Start a server at `localhost:8000` with the model

######`run`: python3 -m allennlp.service.server_simple --archive-path tests/output_dir/model.tar.gz --predictor paper-classifier --include-package my_library  --title "Academic Paper Classifier" --field-name title --field-name paperAbstract

#### https://github.com/allenai/allennlp-as-a-library-example