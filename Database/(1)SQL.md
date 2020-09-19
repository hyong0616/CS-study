# SQL 개요

</br>

## 1. DDL

스키마에 대한 조작을 담당하는 영역

### (1) 명령어

- CREATE : 스키마 생성
- DROP : 스키마 삭제
- ALTER : 스키마 변경

### (2) 무결성 제약

```sql
name varchar(20) not null,
primary key (pID),
foreign key (deptName) references departement,
```

</br>

## 2. DML

인스턴스를 조작하는 영역, query language

### (1) 명령어

- SELECT

>  distinct(중복 제거) default 는 all(중복 허용)

- WHERE
- FROM

> a, b → 카타시안곱 연산에 대응됨
>

- GROUP BY
- HAVING
- ORDER BY
- JOIN

> 중복 제거
>

### (2) string 연산

```sql
where name like "%da%" >>%는 *와 같은 의미임...
where name like "100\%" escape '\' >> \ 는 탈출문자
```

### (3) 비교 연산

- some(=any) : 속한다
- all : 모든 원소 비교
- exists : 존재여부

### (4) DB 변경

- delete

```sql
delete from TABLE where value = 20000
```

- insert

```sql
INSERT into TABLE values(a,b,c)
```

- update

```sql
UPDATE TABLE set value = a where value < 20000
```

</br>

## 3. DCL

스키마와 인스턴스를 제외한 다른 객체를 조작하는 언어 

</br>

## 4. Procedural vs Declareative

- 관계 대수는 Procedural Language이다.
- SQL 언어는 non-procedural Language이다.

</br>

## 5. 널 값

SQL 에서는 세 값 논리를 사용 1, 0, 0.5 라고 생각하면 좋다. 

> true, false, unknown

- AND = minimum 연산
- OR = maximum
- NOT = (1 - value)