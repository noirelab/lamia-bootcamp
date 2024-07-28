nums = [1, 2, 3] # 1 = nums[0], 2 = nums[1] , 3 = nums[2]
print(type(nums))

nums.append(3) # adiciona um elemento no final da lista
nums.append(4)
nums.append(500)
print(len(nums)) # tamanho da lista

print(2 in nums)

nums[3] = 100 # altera o valor do índice 3
nums.insert(0, -200) # insere na posição 0

print(nums[-1]) # acessa o último elemento

print(nums)
print()

# Exemplo próprio -
nums.append(1000)
print(nums)
print(len(nums))
print(132 in nums)
