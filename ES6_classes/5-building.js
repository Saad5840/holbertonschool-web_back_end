// 5-building.js
export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;

    // Ensure that any subclass implements evacuationWarningMessage
    if (this.constructor !== Building && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // getter
  get sqft() {
    return this._sqft;
  }

  // abstract method placeholder
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
