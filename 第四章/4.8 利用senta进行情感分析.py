import json
import os
import six
import paddlehub as hub

# 加载senta_bilstm模型，首次加载会自动下载模型数据
senta = hub.Module(name="senta_bilstm")
# 待测试的文本
test_text = ["这家餐厅很好吃", "这个手机速度很快，就是拍照像素太低了"]
# 构造输入字典
input_dict = {"text": test_text}
# 调用senta的sentiment_classify方法获得情感分析结果
results = senta.sentiment_classify(data=input_dict)
# 输出结果
print(results)