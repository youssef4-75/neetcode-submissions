class Solution {
    public String minAnagram(String s){
        char[] ac = s.toLowerCase().toCharArray();
        Arrays.sort(ac);
        return new String(ac);
    }


    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> lmap = new HashMap<>();
        for(String str: strs){
            String min = minAnagram(str);
            List<String> ls = lmap.getOrDefault(min, new ArrayList<>());
            ls.add(str);
            lmap.put(min, ls);
        }

        for(Map.Entry<String, List<String>> e: lmap.entrySet()){
            result.add(e.getValue());
        }
        
        return result;
    }
}
