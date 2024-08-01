def arithmetic_arranger(problems, display_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    top_operands = []
    bottom_operands = []
    operators = []

    # Parsing and validation
    for problem in problems:
        parts = problem.split()

        # Validate the operator
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validate the operands
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Validate operand length
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        top_operands.append(parts[0])
        operators.append(parts[1])
        bottom_operands.append(parts[2])

    widths = []
    for i in range(len(problems)):
        width = max(len(top_operands[i]), len(bottom_operands[i])) + 2
        widths.append(width)

    top_row = ""
    bottom_row = ""
    dashes_row = ""
    answers_row = ""
    for i in range(len(problems)):
        top_row += top_operands[i].rjust(widths[i]) + "    "
        bottom_row += operators[i] + bottom_operands[i].rjust(widths[i] - 1) + "    "
        dashes_row += "-" * widths[i] + "    "
        if display_answers:
            if operators[i] == "+":
                answer = str(int(top_operands[i]) + int(bottom_operands[i]))
            else:
                answer = str(int(top_operands[i]) - int(bottom_operands[i]))
            answers_row += answer.rjust(widths[i]) + "    "

    arranged_problems = (
        top_row.rstrip() + "\n" + bottom_row.rstrip() + "\n" + dashes_row.rstrip()
    )
    if display_answers:
        arranged_problems += "\n" + answers_row.rstrip()

    return arranged_problems


# Sample Usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
