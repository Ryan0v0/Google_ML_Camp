# ‘ICalligraph’ Customized Chinese Fonts  Generating & Sharing Platform

### Project of Team Aelous in Google ML Winter Camp 2020, PEK

13 - 17 January, 2020

Project Name: I❤️Calligraph

Team Members: Ziyu Zhu, Wanru Zhao, Xinrui Yu

## Installation

```
$ pipenv install --dev --pypi-mirror https://mirrors.aliyun.com/pypi/simple
$ pipenv shell
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## Dataset
1. 王羲之 兰亭集序
2. Other 28 fonts generated by .ttf file
3. User written fonts

## Main Model
![image-20200117113334666](https://tva1.sinaimg.cn/large/006tNbRwly1gazjmoim9gj30xq0jiwj2.jpg)

## Deployment

![image-20200117113420101](https://tva1.sinaimg.cn/large/006tNbRwly1gazjnvox0xj31mc0pok0j.jpg)

## User Interface
![4.2初始用户登录界面](https://tva1.sinaimg.cn/large/006tNbRwly1gazjobaud5j31c00u0qd6.jpg)

![4.4添加评论52.17 AM]https://tva1.sinaimg.cn/large/006tNbRwly1gazjoo7f1jj31c00u0777.jpg)



![image-20200117113628652](https://tva1.sinaimg.cn/large/006tNbRwly1gazjozy3eoj30wy0i6gnj.jpg)

## Examples

庞中华行书：
![评委真帅](https://github.com/Ryan0v0/Google_ML_Camp/blob/master/ICalligraph/static/images/评委真帅.png)

王羲之书法：（dataset from《兰亭集序》）
![大道不器](https://github.com/Ryan0v0/Google_ML_Camp/blob/master/ICalligraph/static/images/大道不器.png)

用户个人手写体：

![谷歌机器学习]
(https://github.com/Ryan0v0/Google_ML_Camp/blob/master/ICalligraph/static/images/谷歌机器学习.png)


![冬令营](/Users/zhaowanru/class/google/ICalligraph/ICalligraph/static/images/冬令营.png)

## References
[1] zi2zi https://github.com/kaonashi-tyc/zi2zi

[2] Cycle Gan https://github.com/junyanz/CycleGAN

[3] https://arxiv.org/abs/1712.00516

[4] https://arxiv.org/pdf/1910.04987.pdf
