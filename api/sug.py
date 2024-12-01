import transformers
import torch
import re

model_name = "Salesforce/codegen-350M-mono"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

def gen_sug(prompt, max_length=128, num_return_sequences=1):
  inputs = tokenizer(prompt, return_tensors="pt")
  outputs = model.generate(
      **inputs,
      len=len,
      return_seq=return_seq,
      do_sample=True,
      top_k=50,
      top_p=0.95,
  )
  sugg = tokenizer.batch_decode(outputs, skip_special_tokens=True)
  return sugg


def code(code):
  try:
    compile(code, '<string>', 'exec')
    if not re.search(r'def\s+calculate_average', code):
      return "Error"
  except SyntaxError as e:
      return f"Syntax error: {e}"
  return "No issues found"

prompt = """
def calculate_average(numbers):
  """
suggestions = gen_sug(prompt)

for sugg in suggestions:
  print(f"Suggestion: {sugg}")
  lint_result = code(sugg)
  print(f"Linting Result: {lint_result}")
  print("---")
