#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    // Swap the values of width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
