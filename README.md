# ERD
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/112c1d4a-d4f6-4354-83f0-e9996219ef45)

# Accounts 기능

### 회원가입
###### Endpoing: /api/accounts
###### Method: POST
###### 조건: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력
###### 검증: username과 이메일은 유일
###### 구현: 데이터 검증 후 저장
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/6bf9b025-4c51-40e2-9812-4ccb8622e23e)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/7150730c-afe0-48f2-be7c-23378df829e1)


### 로그인
###### Endpoing: /api/accounts/login
###### Method: POST
###### 조건: 사용자명과 비밀번호 입력 필요
###### 검증: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함
###### 구현: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메세지를 반환
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/72dbbb75-883b-419b-994e-9ad3e94004b4)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/c4477c34-567c-42c1-a615-e552251d21d1)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/d72151f6-a053-4a11-baa6-8f14db92b228)


### 프로필 조회
###### Endpoing: /api/accounts/<str:username>
###### Method: GET
###### 조건: 로그인 상태 필요
###### 검증: 로그인한 사용자만 프로필 조회 가능
###### 구현: 로그인한 사용자의 정보를 JSON 형태로 반환
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/9e55d99e-bccf-4910-8102-a5e9070f6b27)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/8ed948ee-d408-44b4-831e-cf5fc3c9a4e6)


# Products 기능

### 상품 등록
###### Endpoing: /api/products
###### Method: POST
###### 조건: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요
###### 구현: 새 게시글 생성 및 데이터베이스 저장
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/41ba2ca3-5f53-427f-aa63-52920b98f367)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/c82dff8d-147a-4a62-9dd5-c81873746651)


### 상품 목록 조회
###### Endpoing: /api/products
###### Method: GET
###### 조건: 로그인 상태 불필요
###### 구현: 모든 상품 목록 페이지네이션으로 반환
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/43020da1-2bca-4e57-9e7f-b3966da4c262)


### 상품 수정
###### Endpoing: /api/products/<int:productID>
###### Method: PUT
###### 조건: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능
###### 검증: 요청자가 게시글의 작성자와 일치하는지 확인
###### 구현: 입력된 정보로 기존 상품 정보를 업데이트
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/33f6a01a-d670-4faa-a28a-41a2e7d43052)
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/c6f11190-5d04-4084-9c4a-36bbc2617f08)
###### 작성자와 일치하지 않을 때
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/b965a132-57a7-40e3-bd8f-758717dd4f3b)


### 상품 삭제
###### Endpoing: /api/products/<int:productID>
###### Method: DELETE
###### 조건: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능
###### 검증: 요청자가 게시글의 작성자와 일치하는지 확인
###### 구현: 해당 상품을 데이터베이스에서 삭제
###### 로그인 토큰 안 넣었을 때
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/9c68fd29-7896-4af6-8e84-50abd06a2b21)
###### 원래 목록 조회
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/f80acf64-d72b-4809-8f96-94ba1bca65e5)
###### 삭제하기
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/522d5ff9-1695-4b06-a33c-20a2112cf6ac)
###### 삭제 후 목록 조회
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/06749c90-815a-402f-8a40-3a21baf85c64)
###### 작성자와 다를 때
![image](https://github.com/juhyeon-source/Django_my_second_project/assets/120025871/6761eacb-2870-41f3-9637-627a54caa5ec)
