from django.shortcuts import render

# Create your views here.
from transformers import AutoTokenizer, BertForTokenClassification
from transformers import pipeline


#古长文分句
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
    


#现代文转古文
from transformers import (
  EncoderDecoderModel,
  AutoTokenizer
)
PRETRAINED = "raynardj/wenyanwen-chinese-translate-to-ancient"
tokenizer = AutoTokenizer.from_pretrained(PRETRAINED)
model = EncoderDecoderModel.from_pretrained(PRETRAINED)

import torch

def inference(text):
    tk_kwargs = dict(
      truncation=True,
      max_length=128,
      padding="max_length",
      return_tensors='pt')
   
    inputs = tokenizer([text,],**tk_kwargs)
    with torch.no_grad():
        return tokenizer.batch_decode(
            model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            num_beams=3,
            max_length=128,
            bos_token_id=101,
            eos_token_id=tokenizer.sep_token_id,
            pad_token_id=tokenizer.pad_token_id,
        ), skip_special_tokens=True)

def modern_to_ancient(request):
    if request.method == 'POST':
        modern_sentence = request.POST.get('modern_sentence')
        ancient_sentence = inference(modern_sentence)
        return render(request, 'modern2ancient.html', {'ancient_sentence': ancient_sentence})

    else:
        return render(request,'modern2ancient.html')