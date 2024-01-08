import { Component, OnInit } from '@angular/core';

interface Field {
  label: string;
  value: string;
}

interface LineItem {
  line_number: number;
  items: Field[];
}

interface TableElement{
  header_column: LineItem;
  body_column: LineItem[];
}

class Field {
  static defaultField() {
    return {
      label: '',
      value: ''
    } as Field;
  }
}

class LineItem {
  static defaultLineItem() {
    return {
      items: [Field.defaultField(), Field.defaultField(), Field.defaultField()]
    } as LineItem;
  }
}

class TableElement {
  static defaultTableItem(header_column: LineItem) {
    return {
      header_column: header_column,
      body_column: [LineItem.defaultLineItem()]
    } as TableElement;
  }
}
@Component({
  selector: 'app-transactions',
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.scss']
})
export class TransactionsComponent implements OnInit {

  fields: Field[] = [];
  line_items: LineItem[] = [];

  constructor() { }

  ngOnInit(): void {
  }

  addField() {
    this.fields.push(Field.defaultField());
  }

  addTableElement() {
    this.line_items.push(LineItem.defaultLineItem());
  }

}