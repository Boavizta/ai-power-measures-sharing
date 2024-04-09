### Which csv should I fill ?

Depending on your algorithm, stage & subtask, you have a specific file to use :

| Type of ML algorithm |     stage       | subtask| Doc to fill (.csv or .json) |
| -------------------------- | ------ | ------ | ------ |
| classification          | training or inference  | X| classification_data |
| regression          | training or inference  | X| regression_data |
| xLM          | finetuning or retraining  | X| training_retraining_xLM_data |
| xLM          | inference  | chatbot | inference_xLM_chatbot_data |
| xLM          | inference  | keywords extraction | inference_xLM_keywords_extraction_data|
| xLM          | inference  | summarization | inference_xLM_summarization_data |
| xLM          | inference  | classification | inference_xLM_classification_data |