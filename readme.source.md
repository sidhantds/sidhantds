```aura width=800 height=300
<div style={{ position: 'relative', display: 'flex', width: '100%', height: '100%', background: '#07090f', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', border: '1px solid rgba(255,255,255,0.06)' }}>
  <style>{`
    @keyframes drift-a { 0%, 100% { transform: translate(0,0); opacity: 0.55; } 50% { transform: translate(24px,-18px); opacity: 0.85; } }
    @keyframes drift-b { 0%, 100% { transform: translate(0,0); opacity: 0.45; } 50% { transform: translate(-20px,16px); opacity: 0.7; } }
    @keyframes pulse { 0%, 100% { opacity: 0.25; } 50% { opacity: 1; } }
    @keyframes flow { 0% { stroke-dashoffset: 40; } 100% { stroke-dashoffset: 0; } }
    @keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
    #h-o1 { animation: drift-a 10s ease-in-out infinite; }
    #h-o2 { animation: drift-b 12s ease-in-out infinite 1s; }
    #h-o3 { animation: drift-a 9s ease-in-out infinite 2s; }
    #net { animation: flow 3s linear infinite; }
    #n1 { animation: pulse 3s ease-in-out infinite 0s; }
    #n2 { animation: pulse 3s ease-in-out infinite 0.3s; }
    #n3 { animation: pulse 3s ease-in-out infinite 0.6s; }
    #n4 { animation: pulse 3s ease-in-out infinite 0.9s; }
    #n5 { animation: pulse 3s ease-in-out infinite 1.2s; }
    #n6 { animation: pulse 3s ease-in-out infinite 1.5s; }
    #n7 { animation: pulse 3s ease-in-out infinite 1.8s; }
    #n8 { animation: pulse 3s ease-in-out infinite 2.1s; }
    #h-cur { animation: blink 1.1s step-end infinite; }
  `}</style>

  <svg width="800" height="300" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="hg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(56,139,253,0.45)" />
        <stop offset="100%" stopColor="rgba(56,139,253,0)" />
      </radialGradient>
      <radialGradient id="hg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(45,212,191,0.35)" />
        <stop offset="100%" stopColor="rgba(45,212,191,0)" />
      </radialGradient>
      <radialGradient id="hg3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(139,92,246,0.3)" />
        <stop offset="100%" stopColor="rgba(139,92,246,0)" />
      </radialGradient>
    </defs>
    <ellipse id="h-o1" cx="90" cy="270" rx="240" ry="170" fill="url(#hg1)" />
    <ellipse id="h-o2" cx="690" cy="60" rx="220" ry="160" fill="url(#hg2)" />
    <ellipse id="h-o3" cx="620" cy="280" rx="180" ry="130" fill="url(#hg3)" />

    <g id="net" stroke="rgba(120,170,255,0.22)" strokeWidth="1" strokeDasharray="4 4" fill="none">
      <line x1="560" y1="90" x2="650" y2="70" /><line x1="560" y1="90" x2="650" y2="150" /><line x1="560" y1="90" x2="650" y2="230" />
      <line x1="560" y1="150" x2="650" y2="70" /><line x1="560" y1="150" x2="650" y2="150" /><line x1="560" y1="150" x2="650" y2="230" />
      <line x1="560" y1="210" x2="650" y2="70" /><line x1="560" y1="210" x2="650" y2="150" /><line x1="560" y1="210" x2="650" y2="230" />
      <line x1="650" y1="70" x2="740" y2="110" /><line x1="650" y1="150" x2="740" y2="110" /><line x1="650" y1="230" x2="740" y2="110" />
      <line x1="650" y1="70" x2="740" y2="190" /><line x1="650" y1="150" x2="740" y2="190" /><line x1="650" y1="230" x2="740" y2="190" />
    </g>
    <circle id="n1" cx="560" cy="90" r="5" fill="#58A6FF" />
    <circle id="n2" cx="560" cy="150" r="5" fill="#58A6FF" />
    <circle id="n3" cx="560" cy="210" r="5" fill="#58A6FF" />
    <circle id="n4" cx="650" cy="70" r="5" fill="#2DD4BF" />
    <circle id="n5" cx="650" cy="150" r="5" fill="#2DD4BF" />
    <circle id="n6" cx="650" cy="230" r="5" fill="#2DD4BF" />
    <circle id="n7" cx="740" cy="110" r="5" fill="#A78BFA" />
    <circle id="n8" cx="740" cy="190" r="5" fill="#A78BFA" />
  </svg>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: '0 48px', width: 520, height: '100%' }}>
    <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.4)', letterSpacing: 4, textTransform: 'uppercase' }}>Pune, India</span>
    <span style={{ fontSize: 54, fontWeight: 700, color: '#ffffff', letterSpacing: -2, lineHeight: 1.05, marginTop: 12 }}>Sidhant Pujara</span>
    <div style={{ display: 'flex', alignItems: 'center', marginTop: 14 }}>
      <span style={{ fontSize: 15, color: '#58A6FF', fontFamily: 'monospace' }}>{'> data science intern @ globallogic'}</span>
      <span id="h-cur" style={{ fontSize: 15, color: '#58A6FF', fontFamily: 'monospace', marginLeft: 2 }}>_</span>
    </div>
    <div style={{ display: 'flex', gap: 8, marginTop: 26 }}>
      <span style={{ padding: '5px 14px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.6)', borderRadius: 100, fontSize: 11, border: '1px solid rgba(255,255,255,0.1)', letterSpacing: 1 }}>machine learning</span>
      <span style={{ padding: '5px 14px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.6)', borderRadius: 100, fontSize: 11, border: '1px solid rgba(255,255,255,0.1)', letterSpacing: 1 }}>model deployment</span>
      <span style={{ padding: '5px 14px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.6)', borderRadius: 100, fontSize: 11, border: '1px solid rgba(255,255,255,0.1)', letterSpacing: 1 }}>agentic ai</span>
    </div>
  </div>
</div>
```

```aura width=800 height=230
<div style={{ display: 'flex', flexDirection: 'row', gap: 14, width: '100%', height: '100%', fontFamily: 'Inter, sans-serif' }}>
  <style>{`
    @keyframes live { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.3; transform: scale(0.8); } }
    @keyframes glow { 0%, 100% { opacity: 0.5; } 50% { opacity: 0.85; } }
    #now-dot { animation: live 1.6s ease-in-out infinite; }
    #now-g { animation: glow 6s ease-in-out infinite; }
    #ed-g { animation: glow 7s ease-in-out infinite 1s; }
    #pr-g { animation: glow 8s ease-in-out infinite 2s; }
  `}</style>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', flex: 1, height: '100%', background: '#07090f', borderRadius: 16, overflow: 'hidden', padding: '26px 30px', border: '1px solid rgba(255,255,255,0.06)' }}>
    <svg width="520" height="230" style={{ position: 'absolute', top: 0, left: 0 }}>
      <defs>
        <radialGradient id="ng" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="rgba(56,139,253,0.35)" />
          <stop offset="100%" stopColor="rgba(56,139,253,0)" />
        </radialGradient>
      </defs>
      <ellipse id="now-g" cx="480" cy="220" rx="200" ry="140" fill="url(#ng)" />
    </svg>
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <svg width="10" height="10"><circle id="now-dot" cx="5" cy="5" r="4" fill="#3FB950" /></svg>
      <span style={{ fontSize: 11, color: 'rgba(255,255,255,0.4)', letterSpacing: 3, textTransform: 'uppercase', marginLeft: 8 }}>right now</span>
    </div>
    <div style={{ display: 'flex', flexDirection: 'column', marginTop: 18, gap: 14 }}>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <span style={{ fontSize: 16, fontWeight: 600, color: '#ffffff' }}>Building ML models at GlobalLogic</span>
        <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.45)', marginTop: 3 }}>Data Science Intern, Hitachi group</span>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <span style={{ fontSize: 16, fontWeight: 600, color: '#ffffff' }}>Writing an IEEE paper on Agentic AI</span>
        <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.45)', marginTop: 3 }}>Autonomous agents for supply chain decisions</span>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <span style={{ fontSize: 16, fontWeight: 600, color: '#ffffff' }}>Shipping models to production</span>
        <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.45)', marginTop: 3 }}>FastAPI services, Docker images, AWS</span>
      </div>
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 14, width: 250, flexShrink: 0 }}>
    <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'center', flex: 1, background: '#07090f', borderRadius: 16, overflow: 'hidden', padding: '0 22px', border: '1px solid rgba(255,255,255,0.06)' }}>
      <svg width="250" height="108" style={{ position: 'absolute', top: 0, left: 0 }}>
        <defs>
          <radialGradient id="eg" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(45,212,191,0.35)" />
            <stop offset="100%" stopColor="rgba(45,212,191,0)" />
          </radialGradient>
        </defs>
        <ellipse id="ed-g" cx="230" cy="20" rx="110" ry="80" fill="url(#eg)" />
      </svg>
      <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>education</span>
      <span style={{ fontSize: 15, fontWeight: 600, color: '#ffffff', marginTop: 6 }}>BCA, MIT WPU</span>
      <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.45)', marginTop: 2 }}>Class of 2027</span>
    </div>
    <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'center', flex: 1, background: '#07090f', borderRadius: 16, overflow: 'hidden', padding: '0 22px', border: '1px solid rgba(255,255,255,0.06)' }}>
      <svg width="250" height="108" style={{ position: 'absolute', top: 0, left: 0 }}>
        <defs>
          <radialGradient id="pg" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(139,92,246,0.35)" />
            <stop offset="100%" stopColor="rgba(139,92,246,0)" />
          </radialGradient>
        </defs>
        <ellipse id="pr-g" cx="230" cy="100" rx="110" ry="80" fill="url(#pg)" />
      </svg>
      <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>previously</span>
      <span style={{ fontSize: 15, fontWeight: 600, color: '#ffffff', marginTop: 6 }}>Unified Mentor</span>
      <span style={{ fontSize: 12, color: 'rgba(255,255,255,0.45)', marginTop: 2 }}>Data Science Intern, 2024</span>
    </div>
  </div>
</div>
```

```aura width=800 height=190
<div style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100%', background: '#07090f', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', border: '1px solid rgba(255,255,255,0.06)' }}>
  <style>{`
    @keyframes s-a { 0%, 100% { transform: translate(0,0); opacity: 0.45; } 50% { transform: translate(18px,-12px); opacity: 0.7; } }
    @keyframes s-b { 0%, 100% { transform: translate(0,0); opacity: 0.4; } 50% { transform: translate(-14px,10px); opacity: 0.65; } }
    #s-o1 { animation: s-a 10s ease-in-out infinite; }
    #s-o2 { animation: s-b 12s ease-in-out infinite 1s; }
  `}</style>
  <svg width="800" height="190" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="sg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(56,139,253,0.3)" />
        <stop offset="100%" stopColor="rgba(56,139,253,0)" />
      </radialGradient>
      <radialGradient id="sg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(45,212,191,0.28)" />
        <stop offset="100%" stopColor="rgba(45,212,191,0)" />
      </radialGradient>
    </defs>
    <ellipse id="s-o1" cx="90" cy="160" rx="170" ry="110" fill="url(#sg1)" />
    <ellipse id="s-o2" cx="720" cy="40" rx="160" ry="110" fill="url(#sg2)" />
  </svg>
  <span style={{ fontSize: 11, color: 'rgba(255,255,255,0.3)', letterSpacing: 4, textTransform: 'uppercase', marginBottom: 18 }}>stack</span>
  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 9, justifyContent: 'center', maxWidth: 700 }}>
    {['Python', 'SQL', 'Pandas', 'NumPy', 'scikit-learn', 'Matplotlib', 'Seaborn', 'FastAPI', 'Docker', 'AWS', 'R', 'Java', 'Git', 'Jupyter'].map((t, i) => (
      <span key={i} style={{ padding: '7px 16px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.7)', borderRadius: 100, fontSize: 12, border: '1px solid rgba(255,255,255,0.09)', letterSpacing: 0.5 }}>{t}</span>
    ))}
  </div>
</div>
```

```aura width=800 height=130
<div style={{ display: 'flex', flexDirection: 'row', gap: 14, width: '100%', height: '100%', fontFamily: 'Inter, sans-serif' }}>
  {[
    { label: 'repositories', value: github && github.stats ? github.stats.totalRepos : '—', color: '#58A6FF' },
    { label: 'commits', value: github && github.stats ? github.stats.totalCommits : '—', color: '#2DD4BF' },
    { label: 'stars earned', value: github && github.stats ? github.stats.totalStars : '—', color: '#A78BFA' },
    { label: 'followers', value: github && github.user ? github.user.followers : '—', color: '#F778BA' },
  ].map((s, i) => (
    <div key={i} style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', flex: 1, height: '100%', background: '#07090f', borderRadius: 16, padding: '0 22px', border: '1px solid rgba(255,255,255,0.06)' }}>
      <span style={{ fontSize: 34, fontWeight: 700, color: s.color, letterSpacing: -1 }}>{String(s.value)}</span>
      <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.4)', letterSpacing: 3, textTransform: 'uppercase', marginTop: 6 }}>{s.label}</span>
    </div>
  ))}
</div>
```

```aura width=130 height=44 link="https://sidhantpujara.vercel.app/" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/vercel/ffffff"
  text="Portfolio"
  backgroundColor="#141414"
  width={130}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#ffffff' },
    { offset: '10%', color: '#111111' },
    { offset: '50%', color: '#eeeeee' },
    { offset: '60%', color: '#58A6FF' },
    { offset: '80%', color: '#111111' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

```aura width=130 height=44 link="https://www.linkedin.com/in/sidhant-pujara/" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/linkedin/0A66C2"
  text="LinkedIn"
  backgroundColor="#0a1a2b"
  width={130}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#ffffff' },
    { offset: '10%', color: '#111111' },
    { offset: '50%', color: '#eeeeee' },
    { offset: '60%', color: '#0A66C2' },
    { offset: '80%', color: '#111111' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

```aura width=110 height=44 link="mailto:sidhantpujara@gmail.com" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/gmail/EA4335"
  text="Email"
  backgroundColor="#2b0a0a"
  width={110}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#ffffff' },
    { offset: '10%', color: '#111111' },
    { offset: '50%', color: '#eeeeee' },
    { offset: '60%', color: '#EA4335' },
    { offset: '80%', color: '#111111' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```
