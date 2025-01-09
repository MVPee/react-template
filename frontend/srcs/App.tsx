import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './styles/main.css';

createRoot(document.getElementById('root')!).render(
	<StrictMode>
		<div className="flex justify-center items-center h-screen">
			<div className="bg-red-400 p-8 rounded-lg shadow-lg shadow-red-400">
				<h1 className="text-4xl text-center mb-8 font-medium capitalize text-white">
					React template
				</h1>
				<div className="flex items-center">
					<img src="/favicon.ico" alt="favicon" />
				</div>
			</div>
		</div>
	</StrictMode>
);
