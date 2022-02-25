const solution1 = require("./solution.1.1");
const solution2 = require("./solution.1.2");
const solution3 = require("./solution.2.1");
const solution4 = require("./solution.2.2");

function execute(solution) {
  return function (str) {
    console.log(str);
    res = solution(str);
    console.log(res);
    return res;
  };
}
const exs = [
  "~/{Downloads,Pictures}/*.{jpg,gif,png}",
  "It{{em,alic}iz,erat}e{d,}, please.",
  "thumbnail.{png,jp{e,}g}",
  "nothing to do",
  // 'Ab{{uu,anod}ez,ezret}e{d,{a,b}{ariel{ex,edit},f}} folder.'
];

// exs.map(execute(solution1));
exs.map(execute(solution4));

// expected = ['Abanodezeaarieledit folder.', 'Abanodezeaarielex folder.', 'Abanodezeaf folder.', 'Abanodezebarieledit folder.', 'Abanodezebarielex folder.', 'Abanodezebf folder.', 'Abanodezed folder.', 'Abezreteaarieledit folder.', 'Abezreteaarielex folder.', 'Abezreteaf folder.', 'Abezretebarieledit folder.', 'Abezretebarielex folder.', 'Abezretebf folder.', 'Abezreted folder.', 'Abuuezeaarieledit folder.', 'Abuuezeaarielex folder.', 'Abuuezeaf folder.', 'Abuuezebarieledit folder.', 'Abuuezebarielex folder.', 'Abuuezebf folder.', 'Abuuezed folder.']

// result = ['Abanodezearieledit} folder.', 'Abanodezearielex} folder.', 'Abanodezea} folder.', 'Abanodezeb} folder.', 'Abanodezed} folder.', 'Abanodezef} folder.', 'Abezretearieledit} folder.', 'Abezretearielex} folder.', 'Abezretea} folder.', 'Abezreteb} folder.', 'Abezreted} folder.', 'Abezretef} folder.', 'Abuuezearieledit} folder.', 'Abuuezearielex} folder.', 'Abuuezea} folder.', 'Abuuezeb} folder.', 'Abuuezed} folder.', 'Abuuezef} folder.'];