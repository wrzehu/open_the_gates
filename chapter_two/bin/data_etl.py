import ast
import os

cwd = os.getcwd()
name_of_file = 'text_storage'
directory = os.path.join(cwd, name_of_file)
print(directory)


class DataDictStorage:
    __data_dict = {}
    __i = 1

    def add_data(self, list_of_data):
        """
        Add's values to the dictionary
        :param list_of_data:
        :return: another row in dictionary
        """
        self.load_dict_from_file()
        # change's list to string
        intermediate_list = list(map(lambda x: str(x), list_of_data))

        hash_value = self.__i
        self.__data_dict[hash_value] = intermediate_list
        self.__i += 1

        # Save change to storage
        self.save_dict_to_file()

    def get_has_value(self):
        self.load_dict_from_file()
        return self.__i

    def delete_data(self, hash_value):
        """
        Delete's row in dict
        :param hash_value: id of the row
        """
        self.load_dict_from_file()
        del self.__data_dict[hash_value]
        self.__i -= 1
        self.ordering_keys()

        # Saves data to storage
        self.save_dict_to_file()

    def ordering_keys(self):
        """
        Orders keys after deleting row
        """
        actual_hash_value_list = [x for x in range(1, self.__i)]
        old_hash_value_list = [x for x in self.__data_dict]
        lists_len = len(actual_hash_value_list)
        for i in range(lists_len):
            new_key = actual_hash_value_list[i]
            old_key = old_hash_value_list[i]
            if new_key != old_key:
                self.__data_dict[new_key] = self.__data_dict[old_key]
                self.__data_dict.pop(old_key)

    def get_all(self):
        """
        :return: Whole ordered dictionary
        """
        self.load_dict_from_file()
        return self.__data_dict

    def filter_per_name(self, name):
        """
        Provide keys to filtering base on name
        """
        self.load_dict_from_file()
        ans = []
        for key, value in self.__data_dict.items():
            if value[0] == name:
                ans.append(key)
        return ans

    def filter_per_datetime(self, date_time):
        """
        Provide keys to filtering base on datetiem
         """
        self.load_dict_from_file()
        ans = []
        for key, value in self.__data_dict.items():
            if value[1] == date_time:
                ans.append(key)
        return ans

    def filter_per_description(self, description):
        """
        Provide keys to filtering base on description
        """
        self.load_dict_from_file()
        ans = []
        for key, value in self.__data_dict.items():
            if value[2] == description:
                ans.append(key)
        return ans

    def get_filtered_dict(self, keys_to_disp_list):
        """
        :return Dictionary with filtered values base on provided keys
        """
        some_dict = {str(k): self.__data_dict[k] for k in keys_to_disp_list}
        return some_dict

    def update_data(self, hash_value, list_of_changes):
        """
        Updates data per index
        """
        self.load_dict_from_file()
        before_update = self.__data_dict[hash_value]
        length_of_lists = len(before_update)

        for i in range(length_of_lists):
            if list_of_changes[i] in ['']:
                list_of_changes[i] = before_update[i]
        self.__data_dict[hash_value] = list_of_changes
        self.save_dict_to_file()

    def load_dict_from_file(self):
        """
        Loads dictionary from file
        """

        with open(directory, "r") as file:
            string_rep_of_dict = file.read()
        if string_rep_of_dict == '':
            self.__data_dict = {}
            self.__i = 1
        else:
            some_dict = ast.literal_eval(string_rep_of_dict)
            some_list = [key for key in some_dict]
            some_list.sort()
            some_i = some_list[-1]
            self.__data_dict = some_dict
            self.__i = some_i + 1
        file.close()

    def save_dict_to_file(self):
        """
        Save dict to file
        :return:
        """

        with open(directory, "w") as file:
            file.write(str(self.__data_dict))
            file.close()
