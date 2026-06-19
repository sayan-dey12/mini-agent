import { Command } from "commander";
import { HelloCommand } from "./commands/HelloCommand.js";
import { InduCommand } from "./commands/Indu.js";
const program = new Command();

program
  .name("agent")
  .description("Mini AI Agent")
  .version("1.0.0");

program
  .command("hello")
  .description("Print a greeting")
  .action(() => {
    const command = new HelloCommand();
    command.execute();
  });

  program
  .command("indu")
  .description("A special message for Pomi ❤️")
  .action(() => {
    new InduCommand().execute();
  });

  
export default program;