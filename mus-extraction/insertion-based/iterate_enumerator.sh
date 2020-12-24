find ./test-instances/ -name "*.cnf" | while read filename;
                                do
                                    timeout 120 python insertion-based-extraction.py $filename
                                done
                