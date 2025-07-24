Relative XPATH


1)Courses:


Courses=//a[contains(@class,'rwl3jt-0 my-2')]

Parent_element=//a[text()='Courses']/parent::div

First_Child_element=//a[contains(@class,'rwl3jt-0 my-2')]

second_sibling=//a[contains(@class,'rwl3jt-0 my-2')]/following-sibling::div[1]

href_parent_element=//a[@href='/courses/']/parent::div

ancestor=//a[contains(@class,'rwl3jt-0 my-2')]/ancestor::*

following_sibilings=//a[contains(@class,'rwl3jt-0 my-2')]/following-sibling::*

preceding_elements=//a[contains(@class,'rwl3jt-0 my-2')]/preceding::*



2) Live classes:


Live_Class=//p[text()='LIVE Classes']

parent=//p[text()='LIVE Classes']/parent::div

first_child =//p[text()='LIVE Classes']

second_child=//p[text()='LIVE Classes']/following-sibling::*[1]

ancestor=//p[text()='LIVE Classes']/ancestor::*

following_sibilings=//p[text()='LIVE Classes']/following-sibling::*

preceding_elements=//p[text()='LIVE Classes']/preceding::*


3)Practice:


Practice=//p[@id='practiceslink']

parent=//p[@id='practiceslink']/parent::div

first_child=//p[@id='practiceslink']

second_child=//p[@id='practiceslink']/following-sibling::*[1]

ancestor=//p[@id='practiceslink']/ancestor::*

following_sibilings=//p[@id='practiceslink']/following-sibling::*

preceding_elements=//p[@id='practiceslink']/preceding::*


4) Resources:


Resources=//p[@id='resourceslink']

Parent_class=//p[@id='resourceslink']/parent::div

first_child=//p[@id='resourceslink']

second_Child=//p[@id='resourceslink']/following-sibling::*[1]

ancestor=//p[@id='resourceslink']/ancestor::*

following_sibilings=//p[@id='resourceslink']/following-sibling::*

preceding_elements=//p[@id='resourceslink']/preceding::*


5)Products/Solutions:


Products=//p[@id='solutionslink']

parent_class=//p[@id='solutionslink']/parent::div

first_child=//p[@id='solutionslink']

second_child=//p[@id='solutionslink']/following-sibling::*[1]

ancestor=//p[@id='solutionslink']/ancestor::*

following_sibilings=//p[@id='solutionslink']/following-sibling::*

preceding_elements=//p[@id='solutionslink']/preceding::*


6)Login:


Login=//a[@id='login-btn']

parent_class=//a[@id='login-btn']/parent::div

first_child=//a[@id='login-btn']

href_parent=(//a[@href='/sign-in/']/parent::div)[2]

ancestor=//a[@id='login-btn']/ancestor::*

preceding_elements=//a[@id='login-btn']/preceding::*


7) Sign-up:


sign_up=//a[text()='Sign up']

Parent_class=//a[text()='Sign up']/parent::div

first_child=//a[text()='Sign up']

href_parent=(//a[@href='/register/']/parent::div)[2]

ancestor=//a[text()='Sign up']/ancestor::*

preceding_elements=//a[text()='Sign up']/preceding::*











