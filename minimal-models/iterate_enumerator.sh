find ./test-instances/ -name "*.cnf" | while read filename;
                                do
                                    timeout 120 python enumerator.py $filename
                                done
                