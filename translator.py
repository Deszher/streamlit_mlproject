from transformers import T5TokenizerFast, T5ForConditionalGeneration


# https://huggingface.co/WelfCrozzo/T5-L128-belarusian
class Translator:
    _tokenizer: T5TokenizerFast
    _model: T5ForConditionalGeneration

    PRETRAINED_MODEL_NAME = "WelfCrozzo/T5-L128-belarusian"

    def __init__(self):
        self._tokenizer = T5TokenizerFast.from_pretrained(self.PRETRAINED_MODEL_NAME)
        self._model = T5ForConditionalGeneration.from_pretrained(self.PRETRAINED_MODEL_NAME)

    def translate(self, input: str) -> str:
        encoded_input = self._tokenizer.encode(input, return_tensors='pt')

        result = self._model.generate(encoded_input, return_dict_in_generate=True, output_scores=True, max_length=128)

        encoded_output = result["sequences"][0]

        decoded = self._tokenizer.decode(encoded_output, skip_special_tokens = True, clean_up_tokenization_spaces = True)

        return decoded
