Project participants : 
Hrishikesh Saraf - hsaraf (50205927)
Yash Navin Kumar Jain - yashnavi (50206851)

Copy the contents of source code (.py files) and the input data files into the "Spark" folder of the VM.
Make sure you also copy new_lemmatizer.csv and titanic.csv to spark folder.

Open Terminal in VM
cd spark

*************
For Vignette  
*************
spark-submit --master local[4] TitanicVignette.py

Output : Check the Output.txt file created in spark folder. it should contain the accuracy found out in the pythin script.

********************************
For featured Activity: (Bigram)
********************************
spark-submit --master local[4] BigramFinal.py SampleInput

Note : You can replace Sample Input with the different folder names which we copied from the input folder.

Output :
A folder is created which contains the output. 
Eg for SampleInput folder the output folder is called SampleInputOutput.
   for F2 folder the output created is F2Output.


*********************************
For featured Activity : (Trigram)
*********************************
spark-submit --master local[4] TrigramFinal.py SampleInput

Note : You can replace Sample Input with the different folder names which we copied from the input folder.

Output :
A folder is created which contains the output. 
Eg for SampleInput folder the output folder is called SampleInputOutput.
   for F2 folder the output created is 3gramSampleInputOutput