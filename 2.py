class Dua:
    def process_data(self):
        random_list = [105, 3.1, "hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

        int_data = {'ratuasan': [], 'puluham': [], 'satuan': []}
        float_data = []
        string_data = []

        for item in random_list:
            if isinstance(item, int):
                units = item % 10
                tens = (item // 10) % 10
                hundreds = item // 100
                int_data['ratuasan'].append(hundreds)
                int_data['puluham'].append(tens)
                int_data['satuan'].append(units)
            elif isinstance(item, float):
                float_data.append(item)
            elif isinstance(item, str):
                string_data.append(item)

        print("Data integer (ratusan, puluhan, satuan):", int_data)
        print("Data float:", tuple(float_data))
        print("Data string:", string_data)

Dua_instance = Dua()
Dua_instance.process_data() 