// 2-hbtn_course.constructor_type.test.js
import HolbertonCourse from './2-hbtn_course.js';

describe('HolbertonCourse checks constructor types', () => {
  test('throws error if name is not a string', () => {
    expect(() => {
      new HolbertonCourse(10, 20, ['Lucie', 'Guillaume']);
    }).toThrow();
  });

  test('throws error if length is not a number', () => {
    expect(() => {
      new HolbertonCourse('PHP', '20', ['Lucie', 'Guillaume']);
    }).toThrow();
  });

  test('throws error if students is not an array of strings', () => {
    expect(() => {
      new HolbertonCourse('PHP', 20, 'Not an array');
    }).toThrow();

    expect(() => {
      new HolbertonCourse('PHP', 20, [123, 'Lucie']);
    }).toThrow();
  });

  test('creates object correctly with valid inputs', () => {
    const course = new HolbertonCourse('ES6', 1, ['Bob', 'Jane']);
    expect(course.name).toBe('ES6');
    expect(course.length).toBe(1);
    expect(course.students).toEqual(['Bob', 'Jane']);
  });
});
