// Adaptive UI demo: lightweight learner that updates preference scores based on user actions.
// Stores state in localStorage. Not a production ML model — illustrates adaptive HCI concepts.

const STORAGE_KEY = 'adaptive-ui-state-v1';
const defaultState = {
  compactScore: 0,
  spaciousScore: 0,
  fontSize: 16,
  layout: 'normal' // 'compact' or 'spacious' or 'normal'
};

function loadState(){
  try{
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {...defaultState};
  } catch(e){
    console.error('loadState', e);
    return {...defaultState};
  }
}
function saveState(s){ localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); }

function applyState(s){
  const app = document.getElementById('app');
  // apply layout classes
  app.classList.remove('layout-compact','layout-spacious','layout-normal');
  const layoutClass = s.layout === 'compact' ? 'layout-compact' : (s.layout === 'spacious' ? 'layout-spacious' : 'layout-normal');
  app.classList.add(layoutClass);
  document.documentElement.style.setProperty('--font-size', s.fontSize + 'px');
  // also scale body font
  app.style.fontSize = s.fontSize + 'px';
}

function chooseLayoutByScores(s){
  // simple decision rule: compare scores with small inertia
  if (s.compactScore - s.spaciousScore > 1) return 'compact';
  if (s.spaciousScore - s.compactScore > 1) return 'spacious';
  return 'normal';
}

function recordPreference(s, action){
  // actions: 'toggleCompact','toggleSpacious','incFont','decFont'
  // update scores heuristically
  if (action === 'toggleCompact') s.compactScore += 1;
  if (action === 'toggleSpacious') s.spaciousScore += 1;
  if (action === 'incFont') s.spaciousScore += 0.5;
  if (action === 'decFont') s.compactScore += 0.5;
  // update layout decision
  s.layout = chooseLayoutByScores(s);
  saveState(s);
  applyState(s);
}

function setup(){
  const btnToggle = document.getElementById('toggleLayout');
  const btnInc = document.getElementById('increaseFont');
  const btnDec = document.getElementById('decreaseFont');
  const btnReset = document.getElementById('reset');
  let state = loadState();
  applyState(state);

  btnToggle.addEventListener('click', ()=>{
    // user toggles between compact and spacious — infer their intent
    state = loadState();
    // if currently compact, user likely wants spacious and vice-versa
    if (state.layout === 'compact'){
      recordPreference(state, 'toggleSpacious');
    } else {
      recordPreference(state, 'toggleCompact');
    }
  });

  btnInc.addEventListener('click', ()=>{
    state = loadState();
    state.fontSize = Math.min(24, state.fontSize + 1);
    recordPreference(state, 'incFont');
  });

  btnDec.addEventListener('click', ()=>{
    state = loadState();
    state.fontSize = Math.max(12, state.fontSize - 1);
    recordPreference(state, 'decFont');
  });

  btnReset.addEventListener('click', ()=>{
    state = {...defaultState};
    saveState(state);
    applyState(state);
    alert('Adaptive learner state reset.');
  });
}

window.addEventListener('DOMContentLoaded', setup);
