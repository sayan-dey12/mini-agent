import { Command } from "commander";
import { HelloCommand } from "./commands/HelloCommand.js";
import { TestCommand } from "./commands/TestCommand.js";
import { ChatCommand } from "./commands/ChatCommand.js";
import { ConfigCommand } from "./commands/ConfigCommand.js";

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
  .command("test")
  .description("test the agent package")
  .action(async()=>{
    await new TestCommand().execute();
  })

  program
  .command("chat")
  .description("Start a chat with the AI agent")
  .action(async()=>{
    await new ChatCommand().execute();
  })

  program
  .command("config")
  .description("Configuration of the AI agent (provider , model , mode , temperature)")
  .action(
    async()=>{
      await new ConfigCommand().execute();
    }
  )

  
export default program;