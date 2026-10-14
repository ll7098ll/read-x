/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Pretendard Variable"', 'Pretendard', '"Malgun Gothic"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        serif: ['MaruBuri', '"KoPub Batang"', 'Georgia', 'Batang', 'serif'],
      },
      colors: {
        rx: {
          navy: '#0F172A',
          slate: '#1E293B',
          blue: '#1D4ED8',
          cyan: '#38BDF8',
          teal: '#06B6D4',
          emerald: '#10B981',
          gold: '#FACC15',
          amber: '#F59E0B',
          rose: '#F43F5E',
        },
        paper: {
          ivory: '#FCFBF7',
          sepia: '#F4EFE6',
          night: '#1E293B',
        },
        mastery: {
          mastered: { DEFAULT: '#10B981', soft: '#ECFDF5', text: '#047857' },
          fragile: { DEFAULT: '#F59E0B', soft: '#FFFBEB', text: '#B45309' },
          critical: { DEFAULT: '#F43F5E', soft: '#FFF1F2', text: '#BE123C' },
        },
        trap: {
          d1: '#F43F5E',
          d2: '#F97316',
          d3: '#EAB308',
          d4: '#8B5CF6',
          d5: '#06B6D4',
          d6: '#6366F1',
        }
      },
      boxShadow: {
        'rx-card': '0 2px 12px -2px rgba(15, 23, 42, 0.06), 0 1px 4px -1px rgba(15, 23, 42, 0.04)',
        'rx-header': '0 4px 20px -2px rgba(15, 23, 42, 0.25)',
        'cue-pulse': '0 0 0 4px rgba(250, 204, 21, 0.45)',
      }
    },
  },
  plugins: [],
}
