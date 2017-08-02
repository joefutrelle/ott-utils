import json
import sys
from argparse import ArgumentParser

from ott.class_scores import merge_ml_analyzed
from ott.class_summary import ClassSummary 

if __name__=='__main__':
    ap = ArgumentParser()
    ap.add_argument('count_summary', help='count summary json file')
    ap.add_argument('ml_analyzed_summary', help='ml_analyzed summary json file')
    ap.add_argument('-o', '--output', help='output file')
    args = ap.parse_args()

    with open(args.ml_analyzed_summary) as fin:
        ml_analyzed = json.load(fin)

    with open(args.count_summary) as fin:
        count_summary = json.load(fin)

    merge_ml_analyzed(count_summary, ml_analyzed)

    if args.output is None:
        with open(args.count_summary,'w') as fout:
            json.dump(count_summary, fout)
    else:
        with open(args.output,'w') as fout:
            json.dump(count_summary, fout)