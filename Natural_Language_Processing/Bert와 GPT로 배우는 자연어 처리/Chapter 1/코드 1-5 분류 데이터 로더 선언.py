# 코드 1-5 문서 분류 데이터 로더 선언 예시

"""
from torch.utils.data import DataLoader, RandomSampler
from ratsnlp.nlpbook.classification import NsmcCorpus, ClassificationDataset
corpus = NsmcCorpus()
train_dataset = ClassificationDataset(
    args = args,
    corpus = corpus,
    tokenizer = tokenizer,
    mode = 'train',
)
train_dataloader = DataLoader(
    train_dataset,
    batch_size = args.batch_size,
    sampler = RandomSampler(train_dataset, replacement = False),
    collate_fn = nlpbook.data_collator,
    drop_last = False,
    num_workers = args.cpu_workers,///////
)
"""