import transformers
import torch
model_name = "Salesforce/codegen-350M-mono"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

def suggest(prompt, max_length=128, return_sequences=1):
   inputs = tokenizer(prompt, return_tensors="pt")
  outputs = model.generate(
      **inputs,
      max_len=max_len,
      return_sequences=return_sequences,
      do_sample=True.
      top_k=50,
      top_p=0.95,
  )
  sus = tokenizer.batch_decode(outputs, skip_special_tokens=True)
  return sus

input = """
def calculate_average(numbers):
  """
sug = suggest(input)
print (sug)
