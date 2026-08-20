const fs = require('fs');
const path = require('path');

const SKILL_NAME = 'work-harder-on-yourself';
const SKILL_SOURCE = path.join(__dirname, '..');
const GLOBAL_SKILLS_DIR = path.join(process.env.HOME || process.env.USERPROFILE, '.config', 'opencode', 'skills');
const SKILL_TARGET = path.join(GLOBAL_SKILLS_DIR, SKILL_NAME);

function install() {
  console.log(`Installing ${SKILL_NAME} skill globally...`);
  
  if (!fs.existsSync(GLOBAL_SKILLS_DIR)) {
    fs.mkdirSync(GLOBAL_SKILLS_DIR, { recursive: true });
  }
  
  if (fs.existsSync(SKILL_TARGET)) {
    console.log(`Removing existing installation at ${SKILL_TARGET}`);
    fs.rmSync(SKILL_TARGET, { recursive: true, force: true });
  }
  
  fs.cpSync(SKILL_SOURCE, SKILL_TARGET, { recursive: true });
  console.log(`Skill installed to ${SKILL_TARGET}`);
  
  createSymlinks();
}

function createSymlinks() {
  const opencodeConfigDir = path.join(process.env.HOME || process.env.USERPROFILE, '.config', 'opencode');
  const agentsDir = path.join(opencodeConfigDir, 'agents');
  
  if (fs.existsSync(agentsDir)) {
    const agentDirs = fs.readdirSync(agentsDir, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);
    
    for (const agent of agentDirs) {
      const agentSkillsDir = path.join(agentsDir, agent, 'skills');
      const symlinkPath = path.join(agentSkillsDir, SKILL_NAME);
      
      if (!fs.existsSync(agentSkillsDir)) {
        fs.mkdirSync(agentSkillsDir, { recursive: true });
      }
      
      if (fs.existsSync(symlinkPath)) {
        fs.rmSync(symlinkPath, { force: true });
      }
      
      try {
        fs.symlinkSync(SKILL_TARGET, symlinkPath, 'junction');
        console.log(`Symlinked to agent: ${agent}`);
      } catch (err) {
        console.log(`Could not symlink to agent ${agent}: ${err.message}`);
      }
    }
  }
}

install();