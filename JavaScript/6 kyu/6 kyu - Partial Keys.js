// https://www.codewars.com/kata/5e602796017122002e5bc2ed/train/javascript
// My solution
function partialKeys(obj) {
  const keys = Object.keys(obj).sort();
  return new Proxy(obj, {
    get(target, name) {
      if (name in target) return target[name];
      const key = keys.find((k) => k.startsWith(name));
      if (typeof key !== "undefined") return target[key];
      return undefined;
    },
  });
}

// ...
function partialKeys(obj) {
  let result = Object.assign({}, obj);

  Object.keys(obj)
    .sort()
    .forEach((key) => {
      [...key].reduce((prop, letter) => {
        prop += letter;
        if (!result.hasOwnProperty(prop))
          Object.defineProperty(result, prop, { value: obj[key] });
        return prop;
      }, "");
    });

  return result;
}

// ...
function partialKeys(obj) {
  let keys = Object.keys(obj).sort();
  console.log(keys);
  const obj1 = new Proxy(obj, {
    get: function (target, name, receiver) {
      if (!(name in target)) {
        let regEx = new RegExp("^" + name);
        let key = keys.find((element) => regEx.test(element));
        return key === undefined
          ? undefined
          : Reflect.get(target, key, receiver);
      }
      return Reflect.get(target, name, receiver);
    },
  });
  return obj1;
}
