# About the Package
## Author's Words

Welcome to **the first Edition of the _Bireyselvalue_ Algorithm** official documentation. I am Dr. Deniz Dahman 
the creator of the BireyselValue algorithm and the author of this package. In the following section you 
will have a brief introduction on the principal idea of the BireyselValue algorithm. 
In addition, a reference to the academic publication on the method. Before going ahead, I would like 
to let you know that I have done this work as an independent scientist without any fund or similar capacity. 
I am dedicated to proceeding and seek further improvement on the proposed method at all costs. 
To this end if you wish to contribute in any way to this work, please find further details  in the contributing section.  
  
## Contributing 

If you wish to contribute to the creator of this method and the author, you may want to check possible ways on: 

> `To Contribute in any way possible, thank you, you can check` :

1. view options to subscribe on [Dahman's Phi Services Website](https://dahmansphi.com/subscriptions/)
2. subscribe to this channel [Dahman's Phi Services](https://www.youtube.com/@dahmansphi)     
3. you can support on [patreon](https://patreon.com/user?u=118924481) 


If you prefer *any other way of contribution*, please feel free to contact me directly on [contact](https://dahmansphi.com/contact/). 

*Thank you*

# Introduction

## The BireyselValue Algorithm
Classification is something that exists in nature in a very mysterious way. In fact, I do believe that 
our evolution in some way is related to the __principle of classification__. See, we like to classify things,
sometimes, we use a set of **adjectives** e.g. the good one, the bad one, the far one the close one, etc. 
Other times, we intend to use a set of **nouns**, i.e. __classifying by group names__, e.g. the A group, 
the South way, etc. That’s weird itself, as I am trying to introduce the definition of classification, 
I did classify two ways already, as if **an infinite circle**. Anyway, see here are two ways we classify things, 
one I called the subjective way of classification using **adjectives**, the second is objective way of classification using **nouns**. These are how society tends to use the principle of classifications using the human language.  
That has been said, there is this magical tool that uses its own independent language, tends to __dissolve__ this 
line of difference between **subjectivism**, and **objectivism**, and that is the use of **mathematics**. 
In mathematics, we tend to convert everything into set of numbers, yet to understand the _behavior_ and the _structure_
of those numbers, and finally, we just see how things are grouped.  
To this end, I introduce **a new method of classification** that is **BireyselValue Algorithm**. _Bireysel_ in Turkish language it means **(individual, personal)**. The method is structured based on _three blocks_, 
- [x] the building block, 
- [x] the training block, 
- [x] and the prediction block.  

It basically, relays on **4 characteristics**, I call them _the personal profile_. To learn the details of this method please check out _the official academic publication_ found in the reference.   

## bireyselvalue package __version__1.0
As scientists we must be **skeptical**. Not in a destructive way but in a constructive way, so to speak. 
So, the best approach to be a constructive scientist is to build your research first in an **abstract way** 
then in a **concrete way**. To this end, I have proposed the method and its structure, yet, I had to introduce 
a _concrete_ measure on that proposal, and that is **the purpose of this package**. This package is the _first edition_
of the BireyselValue Algorithm, official released name **bireyselvalue**. This package will serve as a **testing** tool 
on the proposed method, of its first edition. In other words, **not yet for a production capacity**, but rather for 
**research and development** purposes ONLY. The essential finding on accuracy of prediction is _very much promising_. 
In future releases, enhancement of extra features will be added, and yet to be tested. 
To this end, you may feel free to follow the set-up instructions as the following sections suggest. 

# Installation 
> [!TIP]
> The first edition bireyselvalue is tested on several **problematic** datasets. What I mean by problematic is 
a dataset with **extreme overlapping behaviors** across classes and has **insufficient** classification **accuracy** 
using other classification methods. Those sets have various dimensions that go as high as _13000 observations_ 
and _36 variables_. I employed the method using a very **basic machine capacity** that today’s industry can offer. 
To conclude, you **don’t need any advanced hardware capacity** but only basic ones. 
In addition, you make sure you have Python 3 or above version.

## Install bireyselvalue
to install the package all what you have to do:
```
pip install bireyselvalue
```
You should then be able to use the package. You may want to confirm the installation

```
pip show bireyselvalue
```
The result then shall be as:

```
Name: bireyselvalue
Version: 1.0.0
Summary: TEST ON V.1 of THE BireyselValue Algorithm FOR CLASSIFICATION PROBLEMS
Home-page: https://github.com/dahmansphi/bireyselvalue_v1
Author: Dr. Deniz Dahman's
Author-email: dahmansphi@gmail.com
```

## Employ the bireyselvalue -**Conditions**

> [!IMPORTANT]
> It’s mandatory, to use the first edition of bireyselvalue, to make sure the training dataset meets the conditions: 
> 1. Number of observations > 40 per class 
> 2. Number of variables >= 2 
> 3. Number of classes >= 2. 

> Once these conditions are met then you may employ the bireyselvalue. Anyway, the package has a condition built in to make sure those conditions are met. 

As I have mentioned in the introduction, there are **three blocks** for the bireyselvalue 
to make _the final prediction_. Essentially, we need a _training dataset_ that the package will **build**, 
then **train**. Eventually, we call on the **predict_test** to test the result. 
Since this is the **first edition** as a testing block for the method, you will see that 
the only _active_ function for prediction is **predict_test**. To this end you need to make sure:
> 1. The **training** dataset is **separated** from the class vector. i.e. you should have the _ds_ and the _cls_. Where the shape of _ds_ should be **m x n** and the _cls_ should be **m x 1**  
> 2. The **test** dataset is **separated** from the class vector. i.e. you should have the **ds_test** and the **cls_test**. Where the shape of **ds_test** should be **m x n** and the **cls_test** should be **m x 1**. 
> 3. both training and testing dataset shall be of **numpy** type dataset.

## Detour in the bireyselvalue package- Build-in
Once your installation is done, and you have met all the conditions, then you may want to check 
the build-in functions of the bireyselvalue and understand each.  
Essentially, if you create an instance from the bireyselvalue as so: 

```
from bireyselvalue.bireyselvalue import BireyselValue
inst = BireyselValue()
```
now this **inst** instance offers you access to those build in functions that you need. 
this is a screenshot:

![Screenshot of build-in functions of the bireysel_algo.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/bireysel_funs.png)

Once you have bireyselvalue instance, here are the details of the right sequence to employ the bireyselvalue:

### first step:
the train block. you must and option:
1. **MUST** call the `input_feature()` which expect two args the _ds_ and the _cls_ vector class
2. **OPTION** you can call `report_input()` which will give a comrehensive report on the ds and visual graph on 
the class overlapping status, see the screenshots below
3. **MUST** you call `build()` this main function expects one argument that is the radius which must 
be within range
0.1 <= r <= 0.99. the function of the radius can be understood from the acadamic publication of 
the bireyselvalue algorithm refere to the reference
4. **OPTION** you may cal `build_report()` this function expect arg as number that will display a sample of 
the neighbors list. once again you may want to the check the publication paper to understand the ns. 
5. **MUST** you cal `train()` this is the third main function that will do the train process
6. **OPTION** you may call `model_summary()` this function will give you a detail summary on the model 

![Screenshot of the first sequence to employ the bireyselvalue.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/train.png)

![Screenshot of the output from the report_input().](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/input_report_train.png)

![Screenshot of the output from the report_input().](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/class_over_lapping.png)

### second step:
once you have your model and all the report and summary details then you are ready. so you have to call then
the `save_model()` which expects of course the path to where to save

![Screenshot of the save model_model() fun.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/save.png)

### third step:
of course it's time now to load that saved model which hass the 5 parameters the bireyselvalue relays on.
we first of course create a new instance from the `BireyselValue` then call the `load_model()`. you have 
an option to view the details on that loaded model as well calling the `loaded_model_summary()`.
screenshots illustrate that.

![Screenshot of the load_model() fun.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/load.png)
![Screenshot of the summary_load_model() fun.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/summary_loaded_model.png)

### Fourth step

finally what you aim for, the classification step calling `predict_test()` this function expect two args:
the test_ds, and the cls_test vector. the reason that is only predicting test is explaind below sections. 
resul as the graph illustrates
![Screenshot of the test_model() fun.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/test.png)

![Screenshot of the test_model() fun.](https://raw.githubusercontent.com/dahmansphi/bireyselvalue_v1/main/assets/imgs/test_resu.png)




## Optional way to employ bireyselvalue

If you like, I may suggest this way of employing the pacakge, for testing purpose.
basically we can relay on creatin functions. follow the steps as:

- [x] create a training function
- [x] create a save model function
- [x] create a load model function
- [x] create a test model function

and finaly you may call `main()` function on each one. Otherwise you may also use `Class`, all as you wish.

Lest's see each function in action:
### training functino
the training function expects **four args**:
1. the training ds
2. the training class vector
3. the radius number `0.1 <= r <= 0.99`
4. number of report `neighbors, assume 5` 

Now, if **elements 3, and 4** sound foreign to you, you should read the academic publication on 
the method to understand their functions. Once that is done then you expect the function `returns` **instance** of the bireyselvalue that is **build and trained**. Technically speaking, that is **the model to save**. 

```
def train_bp_a(ds, cls, radius, report_num):
    '''this is the first main function on using this package, it expects 
    the ds, cls, and radius, and how many report you wish to see from the neighbors parameter. 
    it basically return the model for saving purpos
    '''
    inst = BireyselValue()
    inst.input_feature(ds=ds, cls=cls)
    inst.report_input()
    inst.build(radius=radius)
    inst.build_report(num=report_num)
    inst.train()
    inst.model_summary()
    
    return inst
```
    

### saving model function
This function will save **the returned model** from the training section. 
It expects two args and that is **the model** and the **path to save to**.

```
def save_model(inst,path_save):
    '''this function basically save the bp_a.v.1.0 model, requrist two args:
        1. the model to save that should be bp_a model instance
        2. the path of saving the model
    '''
    inst.save_model(file_name=path_save)
```
### loading model function
as the name suggests, we are going to load the model. the function expects ONE **arg**:
the **path to load from**, and it `returns` **that model**.

```
def load_model(path_load):
    '''this function basically load the bp_a.v.1.0 model and return it, requires the path of the model to load'''
    model_path = path_load
    model = BireyselValue()
    model.load_model(model_path=model_path)
    model.loaded_model_summary()
    return model
```

### testing prediction function
this is the final function to test the model. basically this function expects three args:
the **model** which has been loaded, the **test dataset**, and finally the **vector class**.
that is done then you feed all to the function, and you expect the result will be printed on the terminal.

```
def test_bp_a(model, ds_test, cls_test):
    '''this function execute the test on bp_a. requires:
        1. model
        2. ds test
        3. cls test
        both must be following the loaded model summary
    '''
    model.predict_test(input_test_feature=ds_test, cls_test_feature=cls_test)
```
Finally, you expected a printed report with accuracy on the terminal as:

```
__________________________________________
*****************END*********************************
predict by neighbors :*********************
[0.30769231 0.         0.69230769]
actul is  2 predict 2
__________________________________________
*****************END*********************************
predict by neighbors :*********************
[0. 0. 1.]
actul is  2 predict 2
__________________________________________
*****************END*********************************
predict by neighbors :*********************
[0.63636364 0.         0.36363636]
actul is  2 predict 0
__________________________________________
*****************END*********************************
```
```
 Your prediction test has accuracy of **94.73684210526315 %**, by neighbors:
```


### call the four functions- `main()`
you may follow this block to on the previous functions:

```
# train model
inst = train_bp_a(ds=ds, cls=cls, radius=0.2, report_num=5)

# save the model
save_model(path_save=path_to_save, inst=inst)

# load model
model = load_model(path_load=path_to_load)

# test model
test_bp_a(ds_test=ds_test, cls_test=cls_test, model=model)
```

## Conclusion on installation and employing 
As I have mentioned, there are strong and promising results, so far, have been shown 
employing the proposed method. The results of accuracy on problematic datasets had ranged 
between 80% up to 98%. I would like to draw your attention to the fact that I **DIDN’T DO ANY CLEANING** 
whatsoever on the datasets. The reason is yet **to prove the potential of the method**. 
In other words, those result of accuracy is just **pure** with no cleaning or similar actions. 
So, what is next?. 

# Future release 

In the future release of the bireyselvalue you expect: 

1. Activation on the rest of four main characteristics of the method, these are: zone characteristic, and column wise characteristic.  
2. Expansion on various types of datasets such as images, and such.  
3. To have extra functions that will take care to prepare the dataset for you instead of manual preparation, such splitting the dataset and class vector.  

Thank you for your interest in trying the method and keep following future releases.

# Reference

please follow up on the project page to find the academic published paper on the method
[bireyselvalue](https://www.authorea.com/users/757119/articles/729250-the-bireyselvalue-a-proposed-method-for-solving-a-classification-problem) project. 
