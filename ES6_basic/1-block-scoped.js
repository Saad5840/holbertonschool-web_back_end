// 1-block-scoped.js
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Do nothing here; don't redeclare or reassign task/task2
  }

  return [task, task2];
}
