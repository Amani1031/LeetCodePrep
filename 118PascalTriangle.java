class Solution {
    
    List<List<Integer>> answer = new ArrayList();
    
    public List<List<Integer>> generate(int n) {
        
        
        // row 1
        List<Integer> row1 = new ArrayList();
        row1.add(1);
        answer.add(row1);
        
        for(int r = 1; r < n; r++){
            List<Integer> newRow = new ArrayList();
            newRow.add(1);
        // r + 1 elements added
            for(int e = 1; e < r; e++){
                List<Integer> prev = answer.get(r-1);
                
                int e1 = prev.get(e-1);
                int e2 = prev.get(e);
                
                newRow.add(e1+e2);
            }
            
            newRow.add(1);
            answer.add(newRow);
        }
        
        return answer;
    }
    
    
}
