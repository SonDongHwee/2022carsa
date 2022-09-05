# 2022carsa
## module 1. Traffic Sign Classifier
> Data Preparation
> * AIHUB 표지판/신호등 데이터셋: <https://aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&dataSetSn=&srchdataClCode=DATACL001&srchOrder=&SrchdataClCode=DATACL002&searchKeyword=%ED%91%9C%EC%A7%80%ED%8C%90>
> 
> croppper를 제작하여 annotation - traffic_sign, bbox좌표를 이용해 추출 (cropper.py)
> <img src="/image/output_2_0.png" width="450px" height="300px" title="data"></img><br/>


> Training
> 
> * class 
> 1. 101(사거리)
> 2. 113(S커브)
> 3. 114(S커브)
> 4. 129(과속방지턱)
> 5. 135(공사중)
> 6. 140(위험)
> 7. 227(정지)
> 8. 302(자전거)
> 9. 306(우회전)
> 10. 307(좌회전)
> 11. 311(U턴)
> 12. 322(횡단보도)
> 13. 324(어린이보호)
> 14. 325(자전거)
> 15. 330(버스전용)
> <br/>
> <img src="/image/prediction.png" width="450px" height="300px" title="data"></img><br/>


## module 2. Delivery Sign Classifier

> Data Preparation
> * 배달 미션은 대회에서 특수 제작되는 표지판으로 학습을 위한 데이터셋이 없다. <br/>
> <img src="/image/DeliverySign.png" width="450px" height="300px" title="data"></img><br/>
> --> One shot Learning 적용해보기.?  <br/>
> -->TODO data generation! 여러 augmentation(RandomRatation, Diffusion, Color-회색조,채도,밝기) 적용 후 annotation 위치에 
