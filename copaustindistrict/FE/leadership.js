const tabs = document.querySelectorAll('[data-tab-target]');
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.tabTarget) //target for the tab that was clicked on
    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active') //Makes all the tabs disappear
    })
    tabs.forEach(tab => {
      tab.classList.remove("active") //Makes all the tabs disappear
    })
    tab.classList.add('active')
    target.classList.add("active"); //make only the tab that is clicked on "active"
  });
});
