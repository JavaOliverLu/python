import pandas as pd 

hero = ["ironman i", "hulk", "iron man ii", "captain america", "thor", "ironman ii"]  
num = [1, 2, 3, 4, 5, 6]

dict = {"電影名稱": hero,  
        "順序": num
        }



select_df = pd.DataFrame(dict)
select_df.sort_values(by = '順序')
