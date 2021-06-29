import argparse
import os

from photon.prelude import Env
from photon.helpers import read_photon_file
from photon.transformer import PhotonTransformer
from photon.statements import CompileState
parser = argparse.ArgumentParser(description = "A hypersafe and fast compiler for the Photon image language")

parser.add_argument("file", type = str)

args = parser.parse_args()


# defining placeholder variables
queries = None
env = None
file = args.file

queries = read_photon_file(file)
env = Env() # only create an env if reading the photon file did not fail
parser = env.create_parser(os.path.abspath("photon/syntax/grammar.lark"))
transformer = PhotonTransformer()

parser_output = parser.parse(queries)
transformed_output: CompileState = transformer.transform(parser_output)
transformed_output.run(env)