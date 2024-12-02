from Report import Report

def GetInput() -> [Report]:
    reports = []
    for line in open('Input.txt', 'r').readlines():
        reports.append(Report([int(x) for x in line.split(' ')]))
    return reports

class PartOne:
    def DoWork(self) -> int:
        valid_reports = 0
        for report in GetInput():
            if report.CheckValidReport():
                valid_reports += 1

        return valid_reports

class PartTwo:
    def DoWork(self) -> int:
        valid_reports = 0
        for report in GetInput():
            if report.CheckValidReport_Task_Two(0, report.levels.copy()):
                valid_reports += 1

        return valid_reports

print(PartOne().DoWork())
print(PartTwo().DoWork())