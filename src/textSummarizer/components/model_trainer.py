from transformers import (
    PegasusTokenizer, 
    PegasusForConditionalGeneration,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments
)
from datasets import load_from_disk
import os
import torch
from src.textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        """
        Initializes the model trainer with configuration.
        """
        self.config = config

    def train(self):
        """
        Loads tokenizer, model, data, and performs training using Seq2SeqTrainer.
        """
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer = PegasusTokenizer.from_pretrained(self.config.model_ckpt)
        model = PegasusForConditionalGeneration.from_pretrained(self.config.model_ckpt).to(device)

        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        dataset = load_from_disk(self.config.data_path)

        training_args = Seq2SeqTrainingArguments(
            output_dir=str(self.config.root_dir),
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_steps=self.config.eval_steps,
            save_steps=int(self.config.save_steps),
            do_eval=self.config.do_eval,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            predict_with_generate=True,
            save_total_limit=2,
            logging_dir=os.path.join(self.config.root_dir, "logs")
        )

        trainer = Seq2SeqTrainer(
            model=model,
            args=training_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"]
        )

        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
