import cape_dataframes as cape
import pandas as pd
import typer
from typing_extensions import Annotated
import os

app = typer.Typer()

def main(
    data_file: str = Annotated[
        str, 
        typer.Option(
            "--data",
            help="The file path of the data file"),
    ], 
    policy_file: str = Annotated[
        str, 
        typer.Option(
            "--policy",
            help="The file path of the privacy policy to be applied"
        )
    ]
) -> None:
    # Read privacy policy 
    policy = cape.parse_policy(policy_file)

    # Read data from file
    df_raw = pd.read_csv(data_file)

    # Apply privacy policy
    df_priv = cape.apply_policy(policy, df_raw)

    # Poate merge sa aplici automat ( privacy folosind doar parametrii din clie.g., epsilon)
    # Si dupa sa detectezi tu automat ce dtype are coloana si apelezi fie Tokenizer (daca e str),
    # fie NumericalPerturbation (daca e int/float)
    # Cv de genul:
    #
    # column_types = pd.dtypes # return series of column name and type in order
    # for idx, col in enumerate(pd.columns):
    #   if column_types[idx] == 'float64' (or 'int64'):
    #       df_priv[col] = NumericalPerturbation(df_raw[col])
    #   elif column_types[idx] == 'string':
    #       df_priv[col] = Tokenizer(df_raw[col]) # also adauga parametrii doriti, care pot sa fie tot din fisier
    # Nush daca e cazu tho pt asta doar daca e timp si sa discuti despre ea in teza (ca ai fct un automatic privacy enhancer)

    # Il salvam cu acelasi nume doar cu subextensia de vrajeala .priv (ca sa se vada diferenta)
    df_priv.to_csv(os.path.splitext(data_file)[0] + '.priv.csv') 


if __name__ == "__main__":
    typer.run(main)