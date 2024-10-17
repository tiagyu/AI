# # 코드 1-3 kcbert-base 모델 준비 예시

# from transformers import BertConfig, BertForSequenceClassification
# pretrained_model_config = BertConfig.from_pretrained(
#     args.pretrained_model_name,
#     num_labels = 2
# )
# model = BertForSequenceClassification.from_pretrained(
#     args.pretrained_model_name,
#     config=pretrained_model_config,
# )