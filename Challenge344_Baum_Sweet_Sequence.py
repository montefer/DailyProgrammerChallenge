# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:39:24 2017

@author: Fernando
"""
def num_to_bin(number):
     bin_bs = "{0:b}".format(number)
     return bin_bs
def baum_sweet_sequence(bs_number_list):
    i=0
    bin_bs = bs_number_list
    while i < len(list(bin_bs)):
        if int(bin_bs[i]) == 0 & int(bin_bs[i])==int(bin_bs[i-1]):
            bin_bs =  bin_bs[1:]
            if int(bin_bs.index('1'))%2==1:
                return 0
            else:
                baum_sweet_sequence(bin_bs)   
        else:
            i+=1
    return 1

if __name__=="__main__":
    baum_sweet_sequence(num_to_bin(20))
            