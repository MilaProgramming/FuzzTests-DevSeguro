import { Builder, By, Key, until } from 'selenium-webdriver';

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        await driver.get('http://localhost:4200/');

        //Usuarios
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-usuario/div[1]/div[1]/button')).click();
        await driver.findElement(By.id('nombre')).sendKeys('Test');
        await driver.findElement(By.id('email')).sendKeys('Test');
        await driver.findElement(By.id('password')).sendKeys('Test');
        await driver.findElement(By.id('confirmPassword')).sendKeys('Test');
        
        await delay(500);
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-usuario/div[1]/div[3]/div/div[2]/button[1]')).click();


        //Cursos
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[1]/button[2]')).click();
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-clase/div[1]/div[1]/button')).click();
        await driver.findElement(By.id('nombre')).sendKeys('Test');
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-clase/div[1]/div[3]/div/div[2]/button[1]')).click();

        //Inscribir
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[1]/button[3]')).click();
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-inscripcion/div/div[1]/select')).sendKeys('Test');
        await driver.findElement(By.xpath('/html/body/app-root/app-home/div/div[2]/app-inscripcion/div/div[2]/div/table/tbody/tr[2]/td[2]/button')).click();

        await delay(4000);
    } finally {
        await driver.quit();
    }
})();
