n, m, k = map(int, input('n,m,k 입력=>').split())
data = list(map(int, input('숫자들 입력=>').split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1

  if m == 0:
    break

  result += second
  m -= 1

print(result)
