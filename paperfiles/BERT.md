# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.

## Notes:
1. BERT: Bidirectional Encoder Representations from Transformer.
2. Key: BERT used markde language model(MLM) to create a deep bidirectional Transformer.
3. Contribution: "Our major contribution is further generalizing these findings to deep bidirectional architectures, allowing the same pre-trained model to successfully tackle a broad set of NLP tasks"
4. There are always two ways to downstream tasks: feature-based and fine-tuning. BERT use fine-tuning to develop model.
5. Down stream work: This work means some featured work when finishing some work such as pre-train and then some specific work. It could include these work: Image classification, Objection ditection, text classification, and others.

5. The structure of paper:
Abstract -> Introduction -> Related Work -> BERT -> Experiments -> Ablation Studies -> Conclusion 

## What direction does this paper belong to ?
This paper belong to deep learning areas.

## What problems does this paper solve ? 
This paper use bidirectional structure rather than unidirection which was firstly created in 2017.

## Why can this method solve this problem ?

## What should we do next

## Conclusion
Today, we always design some model structure to solve some problems. The most way we use is to fine tuning some basic model such as Llama3.1 or others. We could reduce the cost of training model and the cost of time. fine-tuning is an important technoque for us. The competition in Bohrium or Kaggle are also mainly use fine-tuning method to solve.
But we could think more deeply about why BERT was born. The root of it is the ways we can use for down stream work. **Feature base and fine-tuning**, Some people generate these two ideas to find out the way to easily apply the model. Transformer has made a great progress in models. But it use feature base method and this method may not effectiver than fine-tuning. So end-to-end, the BERT appeared.If we could generate the third way to apply, maybe we could design some new models. **If we could notice some new problems and generate some effective method, we may design some new structure of model.**