// https://www.codewars.com/kata/54acc128329e634e9a000362/train/javascript
// My solution
const TCPStateMapper = `
CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED
`.split('\n').reduce((mapper, line) => {
  if (!line.includes(':')) return mapper;
  const [state, event, newState] = line.match(/([^:\->\s]+)/g);
  mapper[state] = (mapper[state] || {});
  mapper[state][event] = newState;
  return mapper;
}, {});

function traverseTCPStates(events) {
  let state = "CLOSED";
  const n = events.length;
  for (let i = 0; i < n; i++) {
    state = TCPStateMapper[state][events[i]];
    if (!state) return 'ERROR';
  }
  return state;
}

// My solution 2
// based on:
// https://www.codewars.com/kata/design-a-simple-automaton-finite-state-machine/train/python

function Automaton(states, start, transtable) {
  return {
    states,
    start,
    run(commands) {
      let state = start;
      const n = commands.length;
      for (let i = 0; i < n; i++) {
        state = state.transition(commands[i], transtable);
        if (!state) return null;
      }
      return state;
    }
  };
}

function State(key, accept=false) {
  return {
    key,
    accept,
    transition(symbol, transtable) {
      return transtable[key][symbol];
    }
  }
}

const EVENT_MAP = `
CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED`.split('\n');

const states = [];
const transtable = {};
for (let i = 0; i < EVENT_MAP.length; i++) {
  const line = EVENT_MAP[i];
  if (!line.includes(':')) continue;
  const [key, event, newKey] = line.match(/[^:\->\s]+/g);
  if (!states.find(x => x.key === key)) states.push(State(key));
  if (!states.find(x => x.key === newKey)) states.push(State(newKey));
  transtable[key] = (transtable[key] || {});
  transtable[key][event] = State(newKey);
}

const a = Automaton(states, State('CLOSED'), transtable);

function traverseTCPStates(eventList) {
  const result = a.run(eventList);
  return result ? result.key : 'ERROR';
}
