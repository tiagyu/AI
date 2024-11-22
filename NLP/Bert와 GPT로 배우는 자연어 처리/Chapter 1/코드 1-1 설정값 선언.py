# # 코드 1-1 설정값 선언 예시

# from ratsnlp.nlpbook.classification import ClassificationTrainArguments
# args = Classification(
# 	pretrained_model_name = 'beomi/kcbert-base',
#     downstream_corpus_name = 'nsmc',
#     downstream_corpus_root_dir = '/root/Korpora',
#     downstream_model_dir = '/gdrive/My Drive/nlpbook/checkpoint-doccls',
#     learning_rate = 5e-5,
#     batch_size = 32,
# )