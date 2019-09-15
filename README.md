# MerkleTree
Program for implementing Merkle Tree and its application

Python Script to calculate Merkle Root of a CSV File Input.
By using a merkle tree, one can validate a large data set contained inside the tree by just comparing the merkle root / root node of the tree.

This script assumes the input data is in the form of CSV File, and saves the finally calculated merkle root for the user in another CSV File.

The data is stored in the leaf nodes and we bubble up from botton to top by calculating the hash of each leaf node.

At the end we are left with a single merkle root capable of validating the whole data set with just a single hash string of 32 bytes.
Merkle Trees reduce the number of computations required for verification of a single component in a large data set as once the tree is created it needs a small amount of information 
(1 hash per level of the tree) to calculate and reach the valid merkle root. As shown in tree.png file.

Program Implementation:-

The File MerkleScript.py will calculate the final hash value for the input.
Input here is given by a example.csv file which contains random hash values generated in python by using sha256() or md5()
and just they are copy paste in  excel file and seperated  by using commas to make multiple enteries in the excel file.

And the other files :-
Hash.py and
text files verify.txt,verify1.txt,verify2.txt,verify3.txt 
are just for reference created by me to calculate randown hash values using particular algorithum and stored it the excel file named 
latish.csv.
By using values in this file e can put it int the example.csv file which is input to the main file.

Performance of the script is fast as it can generate hash values of 1000 enteries in just few seconds.

