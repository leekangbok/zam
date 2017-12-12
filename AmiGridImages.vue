<template>
  <v-layout column>
    <v-flex xs12
      sm6
      offset-sm3>
      <v-container fluid
        grid-list-md
        :class="classObject">
        <v-layout row
          wrap>
          <v-flex v-bind="{ [`xs${card.flex}`]: true }"
            v-for="card in cards"
            :key="card.title">
            <v-card>
              <v-card-media :src="card.src"
                :height="card.height + 'px'">
                <v-container fill-height
                  fluid>
                  <v-layout fill-height>
                    <v-flex xs12
                      align-end
                      flexbox>
                      <span :class="titleClassObject"
                        v-text="card.title"></span>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card-media>
              <v-card-title primary-title>
                <div>
                  <div class="headline">{{card.headline}}</div>
                  <span class="grey--text">{{card.subheadline}}</span>
                </div>
              </v-card-title>
              <v-card-actions :class="actionClassObject">
                <span>자세히 보기</span>
                <!-- <v-spacer></v-spacer> -->
                <v-btn icon
                  @click.native="card.show = !card.show">
                  <v-icon>{{ card.show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
                </v-btn>
              </v-card-actions>
              <v-slide-y-transition>
                <v-card-text v-show="card.show">
                  {{card.detail}}
                </v-card-text>
              </v-slide-y-transition>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    cards: {
      type: Array
    },
    classObject: {
      type: Object,
      default() {
        return {
          grey: true,
          'lighten-4': true
        }
      }
    },
    titleClassObject: {
      type: Object,
      default() {
        return {
          headline: true,
          'white--text': true
        }
      }
    },
    actionClassObject: {
      type: Object,
      default() {
        return {
          white: true
        }
      }
    }
  },
  data() {
    return {}
  }
}
</script>