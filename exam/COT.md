# 1. Turn raw_rows into DataFrame
# 2. Reject all records with invalid scores (NaN, outside range 0-100) with specific, informative error
# 3. Create Student instances from cleaned data
#   - records should be locked
#   - modifying records should raise custom exception
#   - create __str__
#   - create __repr__
#   - create .average() method that returns np.mean of every Student @classmethod
#   - create .lock() method that ensures records are locked @classmethod
#   - create .add_score() method that fails when records are lcoked

paano i convert to list ang string man