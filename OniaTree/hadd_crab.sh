#!/bin/bash -f

indir="/store/group/phys_heavyions/stuli/MCpPb5TeV02/PYTHIA6_Upsilon1SWithFSR_tuneD6T_5TeV02/crab_Analyzer_Ups1SWithFSR_tuneD6T_5TeV02/170327_224351/0000/"
final="OniaTree_Ups1S_PA_5TeV02.root"

/afs/cern.ch/project/eos/installation/cms/bin/eos ls $indir | grep root > list
list2=$(awk -v p=$indir '{print "root://eoscms//eos/cms"p$1}' list)
echo $list2

hadd tmp/stuli/$final $list2

rm -f list
