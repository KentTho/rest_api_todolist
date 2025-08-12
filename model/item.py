# ==============================
#  Class Item (mô tả một To-Do)
# ==============================
class Item:
    def __init__(self, id, title, desc):
        """
        Khởi tạo một đối tượng Item
        :param id: Mã định danh (string)
        :param title: Tiêu đề công việc
        :param desc: Mô tả công việc
        """
        self.id = id
        self.title = title
        self.desc = desc

    def to_json(self):
        """Trả về dạng dict theo cấu trúc mong muốn"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.desc
        }

    def to_json_dict(self):
        """Trả về dict dựa trên thuộc tính của object"""
        return self.__dict__


# Danh sách chứa các To-Do (dùng list tạm, chưa có DB)
toDoList = []

# Thêm dữ liệu mẫu ban đầu
item1 = Item(id="1", title="Learn Flask", desc="Start Learning Flask")
item2 = Item(id="2", title="Learn Spring", desc="Start Learning Spring Framework")

toDoList.append(item1.to_json())
toDoList.append(item2.to_json_dict())