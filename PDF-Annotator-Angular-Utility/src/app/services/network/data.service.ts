import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  headers: HttpHeaders = new HttpHeaders({
    'Content-Type': 'application/json'
  });

  constructor(private http: HttpClient) {}

  doGet(url: string) {
    return this.http.get(url, {
      headers: this.headers
    });
  }

  doPost(url: string, body: any, headers?: HttpHeaders) {
    return this.http.post(url, body, {
      headers: (headers)? headers : this.headers
    });
  }

  doGetPDF(data: string): Observable<Uint8Array | ArrayBuffer> {
    return this.http.get(`/assets/pdfs/${data}.pdf`, { responseType: 'arraybuffer' });
  }
}
