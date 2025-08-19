export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;   // block-scoped
    const task2 = false; // block-scoped
  }

  return [task, task2];
}
