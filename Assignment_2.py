import argparse
from datetime import datetime
import torch
from my_project import GLUEDataModule, GLUETransformer
from pytorch_lightning import Trainer, seed_everything
import argparse


def main(args):
    # Initialize data module and model
    dm = GLUEDataModule(
        model_name_or_path=args.model,
        task_name=args.task,
    )
    dm.setup("fit")

    model = GLUETransformer(
        model_name_or_path=args.model,
        num_labels=dm.num_labels,
        eval_splits=dm.eval_splits,
        task_name=dm.task_name,
    )

    # Initialize the Trainer
    trainer = Trainer(
        max_epochs=args.max_epochs,
        accelerator="auto",
        #gpus=1 if torch.cuda.is_available() else 0,
    )

    # Perform training
    trainer.fit(model, datamodule=dm)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a GLUE task model")
    parser.add_argument("--model", type=str, default="distilbert-base-uncased", help="Model name or path")
    parser.add_argument("--task", type=str, default="mrpc", help="GLUE task name")
    parser.add_argument("--max_epochs", type=int, default=3, help="Maximum number of training epochs")
    # Add more hyperparameters here as needed

    args = parser.parse_args()
    seed_everything(42)
    main(args)
