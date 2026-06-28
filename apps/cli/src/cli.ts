import { Command } from "commander";
import { HelloCommand } from "./commands/HelloCommand.js";
import { InduCommand } from "./commands/Indu.js";
import { TestCommand } from "./commands/TestCommand.js";

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

  program
  .command("test")
  .description("test the agent package")
  .action(async()=>{
    await new TestCommand().execute();
  })

  
export default program;