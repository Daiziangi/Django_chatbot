from django.shortcuts import render

# Create your views here.
from transformers import AutoTokenizer, BertForTokenClassification
from transformers import pipeline



TAG = "raynardj/classical-chinese-punctuation-guwen-biaodian"
ner = pipeline("ner", model=TAG, tokenizer=TAG)

def mark_sentence(x: str):
    outputs = ner(x)
    x_list = list(x)
    for output in outputs:
        x_list.insert(output['end'], output['entity'])
    return "".join(x_list)


def sentence_split(request):
    if request.method == 'POST':
        original_sentence = request.POST.get('original_sentence')
        splited_sentence = mark_sentence(original_sentence)
        return render(request, 'split.html', {'splited_sentence': splited_sentence})

    else:
        return render(request,'split.html')