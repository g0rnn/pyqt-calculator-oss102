import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_number = QGridLayout()
        layout_formula = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        ### 기존의 label 삭제 후 입력과 출력을 통합한 새로운 LineEdit 위젯 생성
        self.formula = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_formula.addRow(self.formula)


        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_modulo = QPushButton("%")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_modulo.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_number.addWidget(button_plus, 4, 3)
        layout_number.addWidget(button_minus, 3, 3)
        layout_number.addWidget(button_product, 2, 3)
        layout_number.addWidget(button_division, 1, 3)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_CE = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_CE.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear 레이아웃에 추가
        layout_number.addWidget(button_modulo, 0, 0)
        layout_number.addWidget(button_CE, 0, 1)
        layout_number.addWidget(button_clear, 0, 2)
        layout_number.addWidget(button_backspace, 0, 3)
        layout_number.addWidget(button_equal, 5, 3)
        
        ### 제곱, 제곱근, 역수 버튼 생성
        button_recip = QPushButton("1/x")
        button_pow = QPushButton("x^2")
        button_root = QPushButton("√")
        
        ### 제곱, 제곱근, 역수 버튼 클릭 시 시그널 설정
        button_recip.clicked.connect(self.button_equal_clicked)
        button_pow.clicked.connect(self.button_equal_clicked)
        button_root.clicked.connect(self.button_equal_clicked)
        
        ### 제곱, 제곱근, 역수 버튼을 layout_number에 추가
        layout_number.addWidget(button_recip, 1, 0)
        layout_number.addWidget(button_pow, 1, 1)
        layout_number.addWidget(button_root, 1, 2)
        
        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                ### x와 y에 저장되는 값을 변경하여 올바르게 배치
                x = (9-number) // 3
                y = (number-1) % 3
                layout_number.addWidget(number_button_dict[number], x+2, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 5, 2)

        ### 00 -> +/-버튼으로 수정
        button_plus_minus = QPushButton("+/-")
        button_plus_minus.clicked.connect(lambda state, num = "*-1": self.number_button_clicked(num))
        layout_number.addWidget(button_plus_minus, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_formula)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.formula.text()
        equation += str(num)
        self.formula.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.formula.text()
        equation += operation
        self.formula.setText(equation)

    def button_equal_clicked(self):
        equation = self.formula.text()
        solution = eval(equation)
        self.formula.setText(str(solution))

    def button_clear_clicked(self):
        self.formula.setText("")

    def button_backspace_clicked(self):
        equation = self.formula.text()
        equation = equation[:-1]
        self.formula.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())