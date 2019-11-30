# Simple Face Recognition with OpenCV

* * *

* OpenCV
OpenCV is one of the most popular library for computer vision. Originally written in C and C++,
it now provides support for Python
* How does it work?
	* OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so 
	complicated, there isn't one simple algorithm that will test if a face was found or not. Instead, there
	are thousands of patterns and features that must be matched. The algorithm breaks the task of identifying
	the face into smaller tasks, each of which is easy to solve. These tasks are called classifiers.
	For something like a face, there would be approximately 6,000 or more classifiers, all of which must
	match for a face to be detected (within error limits). But there is a problem: for face detection, the 
	algorithm starts at the top left of a picture and moves down accross small blocks of data, look at each 
	block, constantly checking if it is a face. Since there are more that 6,000 tests per block, it might have
	millions of calculations to do, which will grind the computer to a halt.
	To get around this problem, OpenCV uses cascades. Like a series of waterfalls, OpenCV cascade breaks the
	problem of detecting fface into multiple stages. For each block, it does a very rough and quick test. If
	it passses, it does a slightly more detailed test, and so on. The algorithm may have 30 to 50 of these stages
	or cascades, and it will only detect face if all stages pass.
	
* Cascade in Practice
	*Though the theory may sound complicated, in practice it is quite simple. The cascades themselves are just a 
	bunch of XML files that contain OpenCV data that is used to detect objects. We can initialize the code with 
	the cascade we want, and then it does the work for us.
	Since face detection is such a common case, OpenCV comes with a number of built-in cascades for detecting
	everything from faces to eyes and hands to legs. There are even cascades for non-human things. 