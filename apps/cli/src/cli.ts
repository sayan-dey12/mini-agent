import { Command } from "commander";
import { HelloCommand } from "./commands/HelloCommand.js";
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

export default program;