package burp;

public class BurpExtender implements IBurpExtender {
	static final String NAME = "{{cookiecutter.project_name}}";

	private IBurpExtenderCallbacks callbacks;

	@Override
	public void registerExtenderCallbacks(IBurpExtenderCallbacks callbacks)
	{
        // keep a reference to our callbacks object
        this.callbacks = callbacks;

        callbacks.setExtensionName(NAME);
				//new XXX(callbacks);
	}
}
