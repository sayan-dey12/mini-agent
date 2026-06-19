import chalk from "chalk";
import boxen from "boxen";
import figlet from "figlet";
import gradient from "gradient-string";
import logSymbols from "log-symbols";

export class HelloCommand {
  execute(): void {
    console.clear();

    // Huge Banner
    console.log(
      gradient.instagram.multiline(
        figlet.textSync("Mini Agent", {
          font: "ANSI Shadow",
          horizontalLayout: "default",
        })
      )
    );

    console.log();

    // Welcome Box
    console.log(
      boxen(
        `${chalk.bold.cyan("🚀 Welcome Back, Sayan!")}

${logSymbols.info} ${chalk.white("AI Status")}      ${chalk.green("Ready")}
${logSymbols.success} ${chalk.white("Provider")}      ${chalk.yellow("Local")}
${logSymbols.success} ${chalk.white("Mode")}          ${chalk.magenta("CLI")}
${logSymbols.success} ${chalk.white("Version")}       ${chalk.blue("v1.0.0")}

${chalk.gray("Your Personal AI Coding Assistant")}`,
        {
          padding: 1,
          margin: 1,
          borderStyle: "double",
          borderColor: "cyan",
          title: " MINI AGENT ",
          titleAlignment: "center",
        }
      )
    );

    console.log();

    // console.log(
    //   chalk.bold.green("Available Commands")
    // );

    console.log();

    // console.log(`${chalk.cyan("agent chat")}       Chat with the AI`);
    // console.log(`${chalk.cyan("agent explain")}   Explain your code`);
    // console.log(`${chalk.cyan("agent search")}    Search documentation`);
    // console.log(`${chalk.cyan("agent browser")}   Open browser`);
    // console.log(`${chalk.cyan("agent tools")}     List installed tools`);
    // console.log(`${chalk.cyan("agent --help")}    Show help`);

    console.log(`${chalk.cyan("agent --help")}    Show help`);


    console.log();

    console.log(
      chalk.gray("────────────────────────────────────────────────────────")
    );

    console.log(
      chalk.yellow("💡 Tip:"),
      chalk.white("Type"),
      chalk.cyan("agent chat"),
      chalk.white("to start talking with your AI.")
    );

    console.log();
  }
}