import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

export const Demo: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const t = frame / fps;
  const signal = interpolate(t, [0.6, 2.6], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const response = interpolate(t, [2.6, 3.2], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const x = width * (0.18 + 0.64 * signal);
  return (
    <AbsoluteFill style={{backgroundColor: '#102b38', color: '#f3faf9',
      fontFamily: 'sans-serif', padding: width * 0.09,
      justifyContent: 'center', gap: height * 0.07}}>
      <div style={{fontSize: width * 0.075, fontWeight: 650, lineHeight: 1.15}}>
        A signal becomes a response.
      </div>
      <svg viewBox={`0 0 ${width} 400`} style={{width: '100%', overflow: 'visible'}}
        role="img" aria-label="Illustrative sensor signal traveling toward an output">
        <path d={`M ${width * 0.18} 200 H ${width * 0.82}`} stroke="#63828b"
          strokeWidth="8" fill="none" />
        <circle cx={width * 0.18} cy="200" r="42" fill="#edbf62" />
        <circle cx={x} cy="200" r="18" fill="#f3faf9" />
        <circle cx={width * 0.82} cy="200" r={42 + response * 20}
          fill={response > 0 ? '#75d7b6' : '#63828b'} />
      </svg>
      <div style={{fontSize: width * 0.038, lineHeight: 1.4}}>
        {t < 2.6 ? 'Sensor input' : 'Output activated'}
        <div style={{fontSize: width * 0.026, marginTop: 24, color: '#afc7cd'}}>
          Illustrative animation
        </div>
      </div>
    </AbsoluteFill>
  );
};
