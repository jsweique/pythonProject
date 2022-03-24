import logging



# 创建日志器
logger = logging.getLogger()

# 创建处理器
sh = logging.StreamHandler()

'''
%(asctime)s 日志发生的时间
%(filename)s 文件名
%(levelname)s 日志级别
%(funcName)s 函数名
%(message)s 日志内容
%(lineno)s 函数的代码行号
'''
# 创建格式器
formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s ')

# 日志器添加处理器
logger.addHandler(sh)

# 处理器设置日志格式
sh.setFormatter(formatter)

# 设置日志输出级别，需要大写
logger.setLevel('DEBUG')

logger.debug('debug级别信息')
logger.info('info级别信息')
logger.warning('warning级别信息')
logger.error('error级别信息')
logger.critical('critical级别信息')

