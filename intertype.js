(function () {
  "use strict";

  /* Elements */
  const chat = document.getElementById("it-chat");
  const input = document.getElementById("it-input");
  const sendBtn = document.getElementById("it-send");
  const stopBtn = document.getElementById("it-stop");
  const backBtn = document.getElementById("it-back");

  const ham = document.getElementById("it-ham");
  const sidebar = document.getElementById("it-sidebar");
  const overlay = document.getElementById("it-overlay");

  const settingsBtn = document.getElementById("it-settings-btn");
  const helpBtn = document.getElementById("it-help-btn");
  const historyBtn = document.getElementById("it-history-btn");
  const profileBtn = document.getElementById("it-profile-btn");

  const settingsModal = document.getElementById("it-settings-modal");
  const helpModal = document.getElementById("it-help-modal");
  const historyModal = document.getElementById("it-history-modal");
  const profileModal = document.getElementById("it-profile-modal");

  const profilePreview = document.getElementById("profile-preview");
  const profileUsername = document.getElementById("profile-username");
  const profileLogo = document.getElementById("profile-logo");
  const profileSaveBtn = document.getElementById("profile-save-btn");

  const darkToggle = document.getElementById("it-dark-toggle");
  const autoreadToggle = document.getElementById("it-autoread-toggle");
  const moonBtn = document.getElementById("it-moon");

  const historyList = document.getElementById("it-history-list");

  /* State */
  let dark = true;
  let autoRead = false;
  let history = [];
  let generating = false;
  let activeCard = null;

  /* Text classification helpers */
  const GREETINGS =
    /^(hi|hello|hey|howdy|hola|gm|gn|ge|yo|sup|namaste|bonjour|greetings|morning|evening|afternoon)(\s|!|\?|$)/i;
  const HELPS =
    /^(help|hlp|assist|support|guide|commands|what.*can.*(you|u)|what.*do)(\s|!|\?|$)/i;
  const TECHNOLY = /^(technoly|technologi|technology|tech)(\s|!|\?|$)/i;

  function isGreeting(text) {
    return GREETINGS.test(text);
  }

  function isHelp(text) {
    return HELPS.test(text);
  }

  function isTechnoly(text) {
    return TECHNOLY.test(text);
  }

  /* Rotating responses */
  const GREETING_RESPONSES = [
    "Meow! 😺 I'm 18 interType, your softlendar AI assistant. Ask me anything about softlendar projects!",
    "Hey there! 🌙 Ready to explore softlendar?",
    "Hi! 😸 What can I help you with today?",
    "Hello! 🦘 Jump into any topic — science, stars, cats, or code!",
    "Greetings! ☀️ Softlendar at your service.",
    "Yo! 🐱 Let's build something curious together.",
    "Hola! 🌟 Ask me about our projects — termirator, ct, wilgo, and more!",
    "Namaste! 🙏 Peace, curiosity, and code.",
  ];

  const HELP_RESPONSES = [
    "I can tell you about:\n• softlendar — our brand and mission\n• termirator — terminal-style web app\n• ct — cat learning platform\n• wilgo — systems language\n• wildo — web framework\n• brose, serch, haster, setomoly, nametermer\n• redarbot, dobart, bylothon — upcoming\n\nJust ask!",
    "Here is what I know:\n• **softlendar** — science, cats, stars, code\n• **termirator** — cyberpunk terminal HUD\n• **ct** — cat-themed learning app\n• **wilgo** + **wildo** — language + framework\n• More projects in the pipeline! 🚀",
    "Ask me about any softlendar project:\ntermirator · ct · wilgo · wildo · brose · serch · haster · setomoly · nametermer · redarbot · dobart · bylothon",
    "Need help? I am your guide to:\n🖥️ termirator — terminal web app\n🐾 ct — cat learning platform\n💻 wilgo / wildo — dev tools\n🔮 redarbot, dobart, bylothon — coming soon",
    "Type a project name or ask a question. I will do my best to answer! 💬",
  ];

  let greetIndex = 0;
  let helpIndex = 0;

  function nextGreeting() {
    const msg = GREETING_RESPONSES[greetIndex];
    greetIndex = (greetIndex + 1) % GREETING_RESPONSES.length;
    return msg;
  }

  function nextHelp() {
    const msg = HELP_RESPONSES[helpIndex];
    helpIndex = (helpIndex + 1) % HELP_RESPONSES.length;
    return msg;
  }

  /* Profile helpers */
  var dbUser = null;
  var dbLogo = null;

  function cacheGet(key) {
    try {
      return localStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }
  function cacheSet(key, val) {
    try {
      localStorage.setItem(key, val);
    } catch (e) {}
  }
  function cacheClear(key) {
    try {
      localStorage.removeItem(key);
    } catch (e) {}
  }

  function updateProfilePreview() {
    const user = dbUser || cacheGet("intertype-user") || "#19";
    const logo = dbLogo || cacheGet("intertype-logo");
    if (logo) {
      profilePreview.innerHTML =
        '<img class="it-profile-avatar" src="' + logo + '" alt="">';
    } else {
      profilePreview.textContent = user;
    }
  }

  function loadProfile() {
    profileUsername.value = dbUser || cacheGet("intertype-user") || "";
    updateProfilePreview();
  }

  function saveProfile() {
    const username = profileUsername.value.trim();
    const file = profileLogo.files[0];

    function persist(logoUrl) {
      dbUser = username || dbUser;
      dbLogo = logoUrl || dbLogo;
      if (username) cacheSet("intertype-user", username);
      if (logoUrl) cacheSet("intertype-logo", logoUrl);
      updateProfilePreview();
      fetch("/api/profile", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: dbUser || "",
          logo_url: dbLogo || "",
        }),
      }).catch(function () {});
      closeModal("profile");
    }

    if (file) {
      const reader = new FileReader();
      reader.onload = function () {
        persist(reader.result);
      };
      reader.readAsDataURL(file);
    } else {
      persist();
    }
  }

  function loadFromServer() {
    fetch("/api/profile")
      .then(function (r) {
        return r.json();
      })
      .then(function (data) {
        if (data.username) {
          dbUser = data.username;
          cacheSet("intertype-user", data.username);
        }
        if (data.logo_url) {
          dbLogo = data.logo_url;
          cacheSet("intertype-logo", data.logo_url);
        }
        updateProfilePreview();
      })
      .catch(function () {
        updateProfilePreview();
      });
  }

  /* Helpers */
  function addMessage(text, isUser) {
    if (!isUser) {
      const div = document.createElement("div");
      div.className = "it-message it-bot";
      div.textContent = text;
      chat.appendChild(div);
      chat.scrollTop = chat.scrollHeight;
      history.push({ role: "bot", text: text, time: Date.now() });
      updateHistoryUI();
      return;
    }

    const wrap = document.createElement("div");
    wrap.className = "it-msg-user-wrap";

    const avatar = document.createElement("div");
    avatar.className = "it-msg-user-avatar";
    const logo = getUserLogo();
    const user = getUserName() || "#19";
    if (logo) {
      avatar.innerHTML =
        '<img class="it-profile-avatar" src="' + logo + '" alt="">';
    } else {
      avatar.textContent = user;
    }

    const col = document.createElement("div");
    col.className = "it-msg-user-col";

    const nameLabel = document.createElement("div");
    nameLabel.className = "it-msg-user-name";
    nameLabel.textContent = user;

    const msg = document.createElement("div");
    msg.className = "it-message it-user";
    msg.textContent = text;

    col.appendChild(nameLabel);
    col.appendChild(msg);
    wrap.appendChild(avatar);
    wrap.appendChild(col);
    chat.appendChild(wrap);
    chat.scrollTop = chat.scrollHeight;
    history.push({ role: "user", text: text, time: Date.now() });
    updateHistoryUI();
  }

  function createAnswerCard(message) {
    const card = document.createElement("div");
    card.className = "it-message it-bot";
    if (message) {
      card.textContent = message;
    } else {
      card.innerHTML =
        '<div class="it-dots"><span></span><span></span><span></span></div>';
    }
    chat.appendChild(card);
    chat.scrollTop = chat.scrollHeight;
    return card;
  }

  function wait(ms) {
    return new Promise(function (resolve) {
      setTimeout(resolve, ms);
    });
  }

  async function send() {
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, true);
    input.value = "";

    const greeting = isGreeting(text);
    const helpReq = isHelp(text);
    const technolyReq = isTechnoly(text);

    generating = true;
    activeCard = createAnswerCard(null);

    if (greeting || helpReq || technolyReq) {
      const delay = greeting ? 3000 : 5000;
      await wait(delay);
      if (!generating) return;
      let reply;
      if (greeting) reply = nextGreeting();
      else if (helpReq) reply = nextHelp();
      else reply = "🏷️ softlendar badge";
      activeCard.textContent = reply;
      history.push({ role: "bot", text: reply, time: Date.now() });
      if (autoRead) speak(reply);
      chat.scrollTop = chat.scrollHeight;
      updateHistoryUI();
      generating = false;
      activeCard = null;
      return;
    }

    await wait(500);
    if (!generating) return;

    try {
      const res = await fetch("/interType/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const data = await res.json();
      if (!generating) return;
      activeCard.textContent = data.reply;
      history.push({ role: "bot", text: data.reply, time: Date.now() });
      if (autoRead) speak(data.reply);
      chat.scrollTop = chat.scrollHeight;
      updateHistoryUI();
    } catch (e) {
      if (!generating) return;
      activeCard.textContent = "*purr* Something went wrong. Try again?";
      history.push({
        role: "bot",
        text: "*purr* Something went wrong. Try again?",
        time: Date.now(),
      });
      if (autoRead) speak("Something went wrong. Try again?");
      chat.scrollTop = chat.scrollHeight;
      updateHistoryUI();
    } finally {
      generating = false;
      activeCard = null;
    }
  }

  function goBack() {
    window.location.href = "/";
  }

  /* Sidebar */
  function openSidebar() {
    sidebar.classList.add("active");
    overlay.classList.add("active");
  }

  function closeSidebar() {
    sidebar.classList.remove("active");
    overlay.classList.remove("active");
  }

  /* Modals */
  function openModal(id) {
    document.getElementById("it-" + id + "-modal").classList.add("active");
  }

  function closeModal(id) {
    document.getElementById("it-" + id + "-modal").classList.remove("active");
  }

  /* Theme */
  function applyTheme() {
    document.body.setAttribute("data-theme", dark ? "dark" : "light");
    if (darkToggle) {
      darkToggle.classList.toggle("on", dark);
    }
  }

  function toggleTheme() {
    dark = !dark;
    applyTheme();
  }

  function toggleAutoRead() {
    autoRead = !autoRead;
    if (autoreadToggle) {
      autoreadToggle.classList.toggle("on", autoRead);
    }
  }

  function speak(text) {
    if (!window.speechSynthesis) return;
    const utter = new SpeechSynthesisUtterance(text);
    utter.rate = 1.1;
    utter.pitch = 1.0;
    window.speechSynthesis.speak(utter);
  }

  /* History UI */
  function updateHistoryUI() {
    if (!historyList) return;
    if (history.length === 0) {
      historyList.innerHTML =
        '<div class="it-history-empty">No chats yet. Start a conversation! 💬</div>';
      return;
    }
    const userMsgs = history.filter(function (h) {
      return h.role === "user";
    });
    if (userMsgs.length === 0) {
      historyList.innerHTML =
        '<div class="it-history-empty">No chats yet. Start a conversation! 💬</div>';
      return;
    }
    historyList.innerHTML = userMsgs
      .map(function (h, i) {
        return (
          '<div class="it-history-item" data-idx="' +
          i +
          '">' +
          escapeHtml(h.text.substring(0, 40)) +
          (h.text.length > 40 ? "..." : "") +
          "</div>"
        );
      })
      .join("");
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  /* Event bindings */
  sendBtn.addEventListener("click", send);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") send();
  });
  stopBtn.addEventListener("click", function () {
    if (generating) {
      generating = false;
      if (activeCard && activeCard.parentNode) {
        activeCard.remove();
      }
      activeCard = null;
    }
    input.value = "";
    input.focus();
  });
  if (backBtn) {
    backBtn.addEventListener("click", goBack);
  }

  if (ham) {
    ham.addEventListener("click", openSidebar);
  }
  if (overlay) {
    overlay.addEventListener("click", closeSidebar);
  }

  document
    .querySelectorAll(".it-sidebar-item[data-view]")
    .forEach(function (item) {
      item.addEventListener("click", function () {
        const view = item.getAttribute("data-view");
        closeSidebar();
        if (view === "settings") openModal("settings");
        if (view === "help") openModal("help");
        if (view === "history") openModal("history");
        if (view === "profile") openModal("profile");
      });
    });

  if (settingsBtn) {
    settingsBtn.addEventListener("click", function () {
      openModal("settings");
    });
  }
  if (helpBtn) {
    helpBtn.addEventListener("click", function () {
      openModal("help");
    });
  }
  if (historyBtn) {
    historyBtn.addEventListener("click", function () {
      openModal("history");
    });
  }
  if (profileSaveBtn) {
    profileSaveBtn.addEventListener("click", saveProfile);
  }

  if (profileBtn) {
    profileBtn.addEventListener("click", function (e) {
      e.preventDefault();
      loadProfile();
      openModal("profile");
    });
  }

  // refresh profile preview on page boot
  loadFromServer();

  document.querySelectorAll("[data-close]").forEach(function (el) {
    el.addEventListener("click", function () {
      closeModal(el.getAttribute("data-close"));
    });
  });

  if (darkToggle) {
    darkToggle.addEventListener("click", toggleTheme);
  }
  if (moonBtn) {
    moonBtn.addEventListener("click", toggleTheme);
  }
  if (autoreadToggle) {
    autoreadToggle.addEventListener("click", toggleAutoRead);
  }

  /* Init */
  applyTheme();
  loadProfile();
  input.focus();
})();
