#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def check_connection(network, first, second):
    graph = [connection.split("-") for connection in network]
    
    future = [first]
    visited = set()
    while future:
        node = future.pop(0)
        for connection in graph:
            if node in connection:
                if second in connection: return True
                visited.add(node)
                future.extend(set(connection) - visited)
                graph.remove(connection)
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
