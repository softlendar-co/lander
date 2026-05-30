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

  const settingsModal = document.getElementById("it-settings-modal");
  const helpModal = document.getElementById("it-help-modal");
  const historyModal = document.getElementById("it-history-modal");

  const darkToggle = document.getElementById("it-dark-toggle");
  const autoreadToggle = document.getElementById("it-autoread-toggle");
  const moonBtn = document.getElementById("it-moon");

  const historyList = document.getElementById("it-history-list");

  /* State */
  let dark = true;
  let autoRead = false;
  let history = [];

  /* Helpers */
  function addMessage(text, isUser) {
    const div = document.createElement("div");
    div.className = "it-message " + (isUser ? "it-user" : "it-bot");
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    if (isUser) {
      history.push({ role: "user", text: text, time: Date.now() });
    } else {
      history.push({ role: "bot", text: text, time: Date.now() });
    }
    updateHistoryUI();
  }

  function showTyping() {
    const div = document.createElement("div");
    div.className = "it-typing";
    div.id = "it-typing";
    div.textContent = "18 interType is typing...";
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    return div;
  }

  function removeTyping() {
    const t = document.getElementById("it-typing");
    if (t) t.remove();
  }

  async function send() {
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, true);
    input.value = "";

    showTyping();

    try {
      const res = await fetch("/interType/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const data = await res.json();
      removeTyping();
      addMessage(data.reply, false);
    } catch (e) {
      removeTyping();
      addMessage("*purr* Something went wrong. Try again?", false);
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
  input.focus();
})();
