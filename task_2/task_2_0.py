import argparse
import logging
from student_exeptions import StudentNameError, InvalidSubjectError, InvalidScoreError
from student import Student

logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)
        
        # Вызываем ошибку класса Student 
        student.add_score('Math', 6)

    except StudentNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e.subject}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e.score}')

if __name__ == '__main__':
    main()