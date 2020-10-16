@echo off

protoc --doc_out=. --doc_opt=markdown,protocol.md *.proto
