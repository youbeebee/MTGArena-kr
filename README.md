﻿## <주의사항>
 * 본 패치는 아레나 클라이언트를 직접 수정합니다. 패치 적용으로 인한 오작동이 있을 수 있으며, 패치 적용시 이에 대한 위험을 감수하는 것으로 간주합니다.
 * 아레나의 폰트가 기존의 Belaren체에서 NotoSans체로 변경됩니다.
 * **적용시 덱 Export 및 Import 기능이 제대로 동작하지 않게 됩니다.**
 * 번역실수 및 버그 제보는 본인에게 해주세요.

## <패치적용방법>
※ 롤백을 위해 패치적용 전 해당 폴더 내의 `resources.assets`와 `sharedassets0.assets` 파일을 다른 곳에 백업해둘 것.

`"수정"` 폴더 내의 파일을 그대로 복사해서 아레나 설치폴더 내의 `MTGA_Data`에 복사한다. (덮어쓸까요?라는 질문에 yes)

 * 설치폴더(기본): `C:\Program Files (x86)\Wizards of the Coast\MTGA\MTGA_Data`

## <롤백방법>
 * 백업해둔 원본 `resources.assets`와 `sharedassets0.assets` 파일을 설치폴더에 다시 덮어씌운다. 
 * `<설치폴더>\Downloads\AssetBundle`에 있는 `data_loc_*.mtga` 파일을 삭제한다.
 * 아레나를 다시 실행한다.


## Change Log
### 190108
* 스플릿카드 테스트: 색출//종극
* "Draw a Card." 문구 번역

### 190107
* 카드 번역 테스트: 아단토 선봉대, 영광의 기사
* 키워드 능력 번역
* 생물을 제외한 서브타입 번역
* 플레인즈워커 카드 테스트: 도미나리아의 영웅 테페리
* 서사시 카드 테스트: 베날리아의 역사
* 플레이버 텍스트 테스트: Ajani's Welcome 등

## TODO
* 카드 이름 한글화?(한글 검색 가능한 경우)
* 생물 타입 한글화
* 쇼크랜드 타입 한글화