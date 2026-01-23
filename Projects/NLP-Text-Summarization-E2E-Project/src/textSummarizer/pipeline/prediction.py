from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
import os


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        # Check if tokenizer exists locally, if not use the base model tokenizer
        if os.path.exists(self.config.tokenizer_path):
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path, local_files_only=True)
        else:
            # Fallback to the base model tokenizer if trained tokenizer doesn't exist
            tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
        
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        # Check if model exists locally, if not use the base model
        if os.path.exists(self.config.model_path):
            pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        else:
            # Fallback to the base model if trained model doesn't exist
            pipe = pipeline("summarization", model="google/pegasus-cnn_dailymail", tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output