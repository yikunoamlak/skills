const fs = require('fs');
const path = require('path');

const SKILL_NAME = 'work-harder-on-yourself';

const OPENCODE_CONFIG_DIRS = [
  path.join(process.env.HOME || process.env.USERPROFILE, '.config', 'opencode'),
  path.join(process.env.APPDATA || '', 'opencode'),
  path.join(process.env.LOCALAPPDATA || '', 'opencode'),
];

function postinstall() {
  console.log(`Post-install: ensuring ${SKILL_NAME} is available globally...`);
  
  for (const configDir of OPENCODE_CONFIG_DIRS) {
    if (!fs.existsSync(configDir)) continue;
    
    const skillsDir = path.join(configDir, 'skills');
    if (!fs.existsSync(skillsDir)) {
      fs.mkdirSync(skillsDir, { recursive: true });
    }
    
    const targetPath = path.join(skillsDir, SKILL_NAME);
    const sourcePath = path.join(__dirname, '..');
    
    if (fs.existsSync(targetPath)) {
      fs.rmSync(targetPath, { recursive: true, force: true });
    }
    
    try {
      fs.symlinkSync(sourcePath, targetPath, 'junction');
      console.log(`Symlinked to ${configDir}/skills/${SKILL_NAME}`);
    } catch (err) {
      try {
        fs.cpSync(sourcePath, targetPath, { recursive: true });
        console.log(`Copied to ${configDir}/skills/${SKILL_NAME} (symlink failed)`);
      } catch (copyErr) {
        console.log(`Failed to install to ${configDir}: ${copyErr.message}`);
      }
    }
  }
  
  console.log('Global installation complete!');
}

postinstall();