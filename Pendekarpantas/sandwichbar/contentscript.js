// Copyright (c) 2010 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var a = /Delivered/gi;
var b = /Received/gi;
var c = /X-Received/gi;
matches = document.body.innerText.match(a&&b&&c);
if (matches) {//call function copyclipboard
  var payload = {
    count: matches.length    // Pass the number of matches back.
  };
  chrome.extension.sendRequest(payload, function(response) {});
  
}
