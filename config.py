import os

class Args:
    currentDir = os.path.dirname(__file__)
    train_path = currentDir + '/data/train.json'
    test_path = currentDir + '/data/test_process.json'
    seq_labels_path = currentDir + '/data/intents.txt'
    token_labels_path = currentDir + '/data/slots.txt'
    bert_dir = 'bert-base-chinese'
    save_dir = currentDir + '/checkpoints/'
    load_dir = currentDir + '/checkpoints/model.pt'
    do_train = True
    do_eval = False
    do_test = True
    do_save = True
    do_predict = True
    load_model = False
    device = None
    seqlabel2id = {}
    id2seqlabel = {}
    with open(seq_labels_path, 'r') as fp:
        seq_labels = fp.read().split('\n')
        for i, label in enumerate(seq_labels):
            seqlabel2id[label] = i
            id2seqlabel[i] = label

    tokenlabel2id = {}
    id2tokenlabel = {}
    with open(token_labels_path, 'r', encoding='UTF-8') as fp:
        token_labels = fp.read().split('\n')
        for i, label in enumerate(token_labels):
            tokenlabel2id[label] = i
            id2tokenlabel[i] = label

    tmp = ['O']
    for label in token_labels:
        B_label = 'B-' + label
        I_label = 'I-' + label
        tmp.append(B_label)
        tmp.append(I_label)
    nerlabel2id = {}
    id2nerlabel = {}
    for i,label in enumerate(tmp):
        nerlabel2id[label] = i
        id2nerlabel[i] = label

    hidden_size = 768
    seq_num_labels = len(seq_labels)
    token_num_labels = len(tmp)
    max_len = 32
    batchsize = 64
    lr = 2e-5
    epoch = 10
    hidden_dropout_prob = 0.1

if __name__ == '__main__':
    args = Args()
    print(args.seq_labels)
    print(args.seqlabel2id)
    print(args.tokenlabel2id)
    print(args.nerlabel2id)