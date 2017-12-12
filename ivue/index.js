import Test from './components/test'

const components = {
  Test
}

export function ivueComponentsRegister(Vue) {
  Object.keys(components).forEach(key => {
    Vue.component(key, components[key])
  })
}
