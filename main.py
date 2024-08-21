def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        merged_string = "".join(file_contents.split())
        result = {}

        for string in merged_string:
             if string in result:
                result[string] += 1
             else:
                result[string] = 1

        def sort_on(dict):
            return dict["num"]
        
        sorted_dict = sorted(result.items(), key=lambda item: item[1])
        list_of_dicts = [{key: value} for key, value in sorted_dict]
        filtered_list_of_dicts = [d for d in list_of_dicts if all(key.isalpha() for key in d)]

  
        for d in filtered_list_of_dicts:
            for key, value in d.items():
              print(f"The {key} character was found {value} times")
        
         



    

    

main()