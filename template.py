def binary_search(l, r):
	'''
	given a function g(m), find the first element such that g(m) is true
	g(m) is a function that exsit m s.t. g(x) is True if x >= m else False

	The key to binary search is DON'T try to find the exact answer, but find
	the split point m such that for all n, n >= m, conditions are satisfied, 
	then m will naturally become the answer for free
	'''
	while l < r:
		m = l + (r - l) // 2
		if f(m):
			return m #optional
		if g(m):
			r = m:
		else:
			l = m + 1
	return l


def tree_with_one_root(root):
	if not root: return ...
	if f(root): return ...
	l = tree_with_one_root(root.left)
	r = tree_with_one_root(root.right)
	return g(root, l, r)

def tree_with_two_root(root1, root2):
	if not root1 and not root2: return ...
	if f(root1, root2): return ...
	c1 = tree_with_one_root(root1.child, root2.child)
	c2 = tree_with_one_root(root.child, root2.child)
	return g(root1, root2, c1, c2)

def bfs():
	q = []
	seen = Set()

	q.append(start)
	seen.add(start)
	steps = 0

	while q:
		size = q.size
		while size > 0:
			state = q.pop(0)
			size -= 1
			if is_goal(state):
				return
			for new_state in expand(state):
				if seen.contains(new_state):
					continue
				q.append(new_state)
				seen.add(new_state)
		step += 1
	return -1