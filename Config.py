
import os
import random




class Config(object):
    
    def __init__(self):
        
        self.mode = 'train'
        # GPU配置
        self.cuda_visible_devices = '0'                           # 可见的GPU
        self.device = 'cuda:0'                                      # master GPU
        self.port = str(random.randint(10000,60000))                # 多卡训练进程间通讯端口
        self.init_method = 'tcp://localhost:' + self.port           # 多卡训练的通讯地址
        self.world_size = 1                                         # 线程数，默认为1
        
        # 训练配置
        self.whole_words_mask = True                                # 使用是否whole words masking机制
        self.num_epochs = 10                                       # 迭代次数
        self.batch_size = 128                                       # 每个批次的大小
        self.learning_rate = 3e-5                                   # 学习率
        self.num_warmup_steps = 0.1                                 # warm up步数
        self.sen_max_length = 96                                   # 句子最长长度
        self.padding = True                                         # 是否对输入进行padding

        # 模型及路径配置
        self.initial_pretrain_model = 'bert-base-uncased'           # 加载的预训练分词器checkpoint，默认为英文。若要选择中文，替换成 bert-base-chinese
        self.initial_pretrain_tokenizer = 'bert-base-uncased'       # 加载的预训练模型checkpoint，默认为英文。若要选择中文，替换成 bert-base-chinese
        self.path_model_save = './checkpoint/bert/'                      # 模型保存路径
        self.path_datasets = './datasets/'                          # 数据集
        self.path_log = './logs/'
        self.path_model_predict = os.path.join(self.path_model_save, 'epoch_4')
