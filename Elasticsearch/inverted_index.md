inverted index
========================
※ Elasticsearch(Hereinafter referred to as ES)
- very versatile data structure
- very easy to use and understand
- Apache Lucene's implementation

# Inverted Indexes and Index Terms
![screenshot](./images/inverted-index.png)  
위의 그림의 세 문장은 몇 가지 프로세스를 거치고(lowercasing, removing punctuation and splitting words), 위의 그림과 같은 "inverted index" 구조가 만들어진다.

"inverted index"는 terms를 포함한 documents (and possibly positions in the document)에 terms를 map한다.
그 terms들은 dictionary에서 정렬되기 때문에, 엘라스틱서치는 빠르게 term을 찾을 수 있고, 그 뒤에 posting-structure에서 해당 용어(의 occurrences)를 찾을 수 있다.
이는 구체적인 document와 연관된 terms을 리스팅하는 "forward index"와 반대되는 개념이다.

여러 용어가 있는 간단한 검색은 모든 용어와 그 존재(occurrences)를 찾아보고 존재의 집합(sets of occurrences)의 교차(intersection for AND searches) 또는 결합(union for OR searches)을 수행하여 결과 document 목록을 가져온다. 

보다 복잡한 쿼리들은 분명 더욱 정교하지만, 접근 방식은 동일하다: 첫째, 후보 용어(candidate terms)를 dictionary에서 찾고, 그리고 해당 존재(occurrences), 위치(positions) 등을 찾는다.

결과적으로, 하나의 index term은 하나의 검색 unit이다. Elasticsearch가 생성한 terms는 Elasticsearch가 효과적으로 할 수 있는 검색의 타입을 좌우한다. 예를 들어, 위의 그림의 dictionary에서, Elasticsearch는 "c"로 시작하는 모든 단어를 효율적으로 찾을 수 있다. 하지만 "ours"를 포함하는 모든 단어에 대하여 효율적인 검색은 수행할 수 없다. 

그러기 위해서는 ES는 "yours" 또한 "ours"를 포함하고 있다는 것을 찾기 위해 모든 용어들을 가로 질러(traverse all the terms)야만 할 것이다. 이는 index가 사소한 경우(trivially small)가 아니라면 굉장히(prohibitively) 비싸다. In terms of complexity, looking up terms by their prefix is \(\mathcal{O}\left(\mathrm{log}\left(n\right)\right)\), while finding terms by an arbitrary substring is \(\mathcal{O}\left(n\right)\).

즉, ES는 용어 접두어(prefixes)가 붙은 것을 효율적으로 찾을 수 있다. 오로지 inverted index만 가지고 있을 때, 모든 것이 문자열 접두사 문제(string prefix problem)처럼 보이길 원한다. 아래는 몇가지 그러한 변형(transformations)의 예이다. 

- "tastic"으로 끝나는 것을 찾기 위해, 우리는 거꾸로 색인할 수 있고("fantastic" -> "citsatnaf"), "citsat"로 시작하는 모든 것을 찾을 수 있다.

- 부분 문자열 찾기(finding substrings)는 종종 용어를 "n-grams"라고 하는 더 작은 용어로 분리하는 것을 포함한다. 예를 들어, "yours"는 "^yo", "you", "our", "urs", "rs$"로 분리될 수 있다. 그리고 그것은 "our"와 "urs"를 검색함으로써 "ours"의 존재(occurrences)를 얻을 수 있다는 의미이다.

- 노르웨이어와 독일어와 같이 복합어(compound words)를 사용하는 언어의 경우, "schiff"를 검색 할 때 "Donaudampfschiff"와 같은 단어의 경우 "donau", "dampf", "schiff"처럼 분해(decompound)할 필요가 있다. 

- (60.6348, 6.5017)과 같은 지리적 좌표 점(geographical coordinate points)은 "u4u8gyykk"과 같은 "geo hashes"로 변환 될 수 있다. 문자열이 길수록 정확도가 높아진다.

- 사람의 이름에 굉장히 유용한 음성[발음] 매칭(phonetic matching)을 가능하게 하기 위해서는, "Smith"를 {"SM0", "XMT"}로, "Schmidt"를 {"XMT", "SMT"}로 변환하는 "[Metaphone](https://en.wikipedia.org/wiki/Metaphone)"과 같은 알고리즘이 있다.