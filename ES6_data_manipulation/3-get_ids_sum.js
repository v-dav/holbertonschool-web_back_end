import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(studentsList) {
  return getListStudentIds(studentsList).reduce((accumulator, currVal) => accumulator + currVal);
}
