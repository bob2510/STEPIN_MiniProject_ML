1) Why did you choose this algorithm?

   There are many good algorithms other than Convolutional Neural Network like SVM, Gaussian Naive Bayes, KNN, Decision Trees, Random Forests and some other that give very good results
   
   but as per my experience in my Final year project, CNN gives the best result for a image classification problem so I chose CNN for this project.
   


2) Why you took any decisions?

   Some of the decisions that I took was to select the batch_size, number of epochs, the sequential model and the loss function
   
   ABout batch_size, usually slightly lower batch sizes are good for a better training and the neural network works better in such a scenario.
   
   Selecting the number of epochs was just a trial and error, increasing epochs higher than this resulted in increasing error. So, epoch of 40 was selected
   
   The combination of Convolution and MaxPool layer is the heart of Convolutional Neural Networks so I applied the basics. And added some dropout layers to increase the training rate.
   
   In the problems like this, where the output can belong to one of the specified classes, this loss fucntion is used because it is designed to tell the difference between two districutions
   

3) How you tackled Problems?

   Took few iterations to settle on number of epochs for a better training.
  
  
4) Results

   There was no need of going to any other algorithm because this algorithm gave more than 94% accuracy which is pretty high 
   ![Kaggle Submission](https://github.com/bob2510/STEPIN_MiniProject_ML/blob/5e5705c8dd85819fd295d282276c91a9ae052414/SET1/digit_recognizer.PNG)
   
   
5) Conclusions

   CNN is a great tool for an image classification problem  
  
  
