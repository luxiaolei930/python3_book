# 导入spacy工具包
import spacy  
 
# 导入英文核心模型 
nlp = spacy.load("en_core_web_sm")  
	  
# 待处理文本  
text = ("When Sebastian Thrun started working on self-driving cars at "
"Google in 2007, few people outside of the company took him "  
"seriously. “I can tell you very senior CEOs of major American "  
"car companies would shake my hand and turn away because I wasn’t "  
"worth talking to,” said Thrun, in an interview with Recode earlier "  
"this week.")  
doc = nlp(text)  
for entity in doc.ents:  
    print(entity.text, entity.label_)