export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    this._sqft = newSqft;
  }

  evacuationWarningMessage() {
    if (this.evacuationWarningMessage === null) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  };
};
