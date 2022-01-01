#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

if __name__ == '__main__':
    pass