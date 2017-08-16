#!/bin/bash -f
# argh! doesn't work

#indir="/store/group/phys_heavyions/stuli/MCpPb5TeV02/PYTHIA6_Upsilon1SWithFSR_tuneD6T_5TeV02/crab_Analyzer_Ups1SWithFSR_tuneD6T_5TeV02/170327_224351/0000/"
indir="/store/group/phys_heavyions/stuli/MCpPb5TeV02/PYTHIA6_Upsilon3S_tuneD6T_5TeV02/crab_Analyzer_Ups3S_tuneD6T_5TeV02/170816_000525/0000/"
final="OniaTree_Ups3S_PA_5TeV02.root"

eos ls $indir | grep root > list
list2=$(awk -v p=$indir '{print "root://eoscms//eos/cms"p$1}' $list)
#/afs/cern.ch/project/eos/installation/ams/bin/eos ls $indieos ls $indir | grep root > list
#list2=$(awk -v p=$indir '{print "root://eoscms//eos/cms"p$1}' list)
echo $list2

#hadd tmp/stuli/$final $list2
hadd /store/group/phys_heavyions/stuli/MCpPb5TeV02/PYTHIA6_Upsilon3S_tuneD6T_5TeV02/$final $list2

rm -f list
