import { Canvas } from '@react-three/fiber';
import { Environment, Float, Sphere, MeshDistortMaterial, MeshWobbleMaterial } from '@react-three/drei';
import { useRef, useLayoutEffect } from 'react';
import * as THREE from 'three';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const FloatingShapes = () => {
  const groupRef = useRef<THREE.Group>(null);

  useLayoutEffect(() => {
    if (!groupRef.current) return;

    // Rotate and move the group based on scroll progress
    ScrollTrigger.create({
      trigger: document.body,
      start: 'top top',
      end: 'bottom bottom',
      scrub: 1,
      onUpdate: (self) => {
        if (groupRef.current) {
          // Full 360-degree rotation across the whole page scroll
          groupRef.current.rotation.y = self.progress * Math.PI * 2;
          // Gentle arc motion up and then down
          groupRef.current.position.y = Math.sin(self.progress * Math.PI) * 2;
        }
      },
    });
  }, []);

  return (
    <group ref={groupRef}>
      {/* Bubble 1 */}
      <Float speed={2} rotationIntensity={1} floatIntensity={2}>
        <Sphere args={[1, 64, 64]} position={[-3, 1, -5]} scale={1.5}>
          <MeshDistortMaterial color="#10b981" envMapIntensity={1} clearcoat={1} clearcoatRoughness={0} metalness={0.1} roughness={0.2} distort={0.4} speed={2} />
        </Sphere>
      </Float>
      
      {/* Bubble 2 */}
      <Float speed={1.5} rotationIntensity={2} floatIntensity={1.5}>
        <Sphere args={[1, 64, 64]} position={[4, -1, -8]} scale={2}>
          <MeshWobbleMaterial color="#f59e0b" envMapIntensity={1} roughness={0.2} metalness={0.1} factor={1} speed={2} />
        </Sphere>
      </Float>

      {/* Bubble 3 */}
      <Float speed={3} rotationIntensity={1} floatIntensity={2}>
        <Sphere args={[1, 64, 64]} position={[1, -3, -4]} scale={1}>
          <MeshDistortMaterial color="#0ea5e9" envMapIntensity={1} clearcoat={1} clearcoatRoughness={0} metalness={0.1} roughness={0.2} distort={0.5} speed={3} />
        </Sphere>
      </Float>
    </group>
  );
};

export default function CanvasBackground() {
  return (
    <div className="absolute inset-0 z-0 pointer-events-none">
      <Canvas 
        camera={{ position: [0, 0, 8], fov: 45 }}
        gl={{ powerPreference: "default", antialias: false, alpha: true }}
        dpr={[1, 1.5]}
      >
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} intensity={1.5} color="#ffffff" />
        <directionalLight position={[-10, -10, -5]} intensity={0.5} color="#10b981" />
        <FloatingShapes />
        <Environment files="/potsdamer_platz_1k.hdr" />
      </Canvas>
    </div>
  );
}
