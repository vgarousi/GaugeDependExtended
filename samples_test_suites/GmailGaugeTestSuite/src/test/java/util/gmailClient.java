package util;

import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp;
import com.google.api.client.extensions.jetty.auth.oauth2.LocalServerReceiver;
import com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeFlow;
import com.google.api.client.googleapis.auth.oauth2.GoogleClientSecrets;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.util.store.FileDataStoreFactory;
import com.google.api.services.gmail.Gmail;
import com.google.api.services.gmail.GmailScopes;
import com.google.api.services.gmail.model.Label;
import com.google.api.services.gmail.model.ListLabelsResponse;
import com.google.api.services.gmail.model.ListMessagesResponse;
import com.google.api.services.gmail.model.Message;
import com.google.api.services.gmail.model.ModifyMessageRequest;
import java.io.ByteArrayOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.security.GeneralSecurityException;
import java.util.Collections;
import java.util.List;
import java.util.Properties;
import javax.mail.Message.RecipientType;
import javax.mail.Session;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import com.google.api.client.repackaged.org.apache.commons.codec.binary.Base64;

public class gmailClient {

  private static final String APPLICATION_NAME = "Gauge Gmail Client";
  private static final JsonFactory JSON_FACTORY = JacksonFactory.getDefaultInstance();
  private static final String TOKENS_DIRECTORY_PATH = "tokens";

  private static final List<String> SCOPES = Collections.singletonList(GmailScopes.GMAIL_MODIFY);
  private static final String CREDENTIALS_FILE_PATH = "/credentials.json";
  private static final String user = "me";

  private static final String SENT_ID = "SENT";
  private static final String UNREAD_ID = "UNREAD";
  private static final String INBOX_ID = "INBOX";

  private static Credential getCredentials(final NetHttpTransport HTTP_TRANSPORT)
      throws IOException {
    // Load client secrets
    InputStream in = gmailClient.class.getResourceAsStream(CREDENTIALS_FILE_PATH);

    if (in == null) {
      throw new FileNotFoundException("RESORCE NOT FOUND" + CREDENTIALS_FILE_PATH);
    }
    GoogleClientSecrets clientSecrets = GoogleClientSecrets
        .load(JSON_FACTORY, new InputStreamReader(in));

    // Build flow and trigger user authorization request.
    GoogleAuthorizationCodeFlow flow = new GoogleAuthorizationCodeFlow.Builder(
        HTTP_TRANSPORT, JSON_FACTORY, clientSecrets, SCOPES)
        .setDataStoreFactory(new FileDataStoreFactory(new java.io.File(TOKENS_DIRECTORY_PATH)))
        .setAccessType("offline")
        .build();
    LocalServerReceiver receiver = new LocalServerReceiver.Builder().setPort(8888).build();
    return new AuthorizationCodeInstalledApp(flow, receiver).authorize("user");
  }

  private static Gmail buildClient() throws IOException, GeneralSecurityException {
    // Build a new authorized API client service.
    final NetHttpTransport HTTP_TRANSPORT = GoogleNetHttpTransport.newTrustedTransport();
    Gmail service = new Gmail.Builder(HTTP_TRANSPORT, JSON_FACTORY, getCredentials(HTTP_TRANSPORT))
        .setApplicationName(APPLICATION_NAME)
        .build();

    return service;
  }

  private static void getSentId(Gmail service) throws IOException {
    ListLabelsResponse labelsResponse = service.users().labels().list(user).execute();
    for (Label label : labelsResponse.getLabels()) {
      System.out.println(label.getName());
    }
  }

  public static void allMessagesMarkedAsRead() throws GeneralSecurityException, IOException {
    Gmail service = buildClient();

    ListMessagesResponse listMessagesResponse = service.users().messages().list(user).execute();
    if(listMessagesResponse.getResultSizeEstimate() == 0){
      return;
    }

    List<String> labelsToRemove = Collections.singletonList(UNREAD_ID);
    for (Message msg : listMessagesResponse.getMessages()) {
      String id = msg.getId();
      ModifyMessageRequest mod = new ModifyMessageRequest().setRemoveLabelIds(labelsToRemove);
      service.users().messages().modify(user, id, mod).execute();

    }
  }

  public static void sendMail(String subject, String body) throws Exception {
    String to = "cboyle51.test@gmail.com";
    String from = "cboyle51.test@gmail.com";
    String host = "localhost";

    Properties properties = System.getProperties();
    properties.setProperty("mail.smtp.host", host);
    Session session = Session.getDefaultInstance(properties);

    MimeMessage msg = new MimeMessage(session);
    msg.setFrom(new InternetAddress(from));
    msg.addRecipient(RecipientType.TO, new InternetAddress(to));
    msg.setSubject(subject);
    msg.setText(body);

    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    msg.writeTo(stream);
    String encodedEmail = Base64.encodeBase64URLSafeString(stream.toByteArray());
    Message message = new Message();
    message.setRaw(encodedEmail);
    message.setLabelIds(Collections.singletonList("INBOX"));

    Gmail service = buildClient();
    message = service.users().messages().send("me", message).execute();

    System.out.println("Message id: " + message.getId());
    System.out.println(message.toPrettyString());

  }

  public static int getMessagesForLabel(String labelId) throws IOException, GeneralSecurityException {
    Gmail service = buildClient();
    ListMessagesResponse listResponse = service.users().messages().list(user).execute();

    int count = 0;
    if( listResponse.getResultSizeEstimate() == 0){
      return 0;
    }

    for (Message msg : listResponse.getMessages()) {
      String id = msg.getId();
      Message fullmsg = service.users().messages().get(user, id).execute();
      System.out.println("Message ID: "+ id);
      System.out.println(fullmsg.getLabelIds());
      if (fullmsg.getLabelIds().stream().anyMatch(label -> label.equals(labelId))) {
        count++;
      }
    }
    return count;
  }

  public static int getSentMessages() throws IOException, GeneralSecurityException{
    try{
      Thread.sleep(1000);
    }catch (InterruptedException e){

    }
    return getMessagesForLabel(SENT_ID);
  }

  public static int getUnreadMessages() throws IOException, GeneralSecurityException {
    return getMessagesForLabel(UNREAD_ID);
  }

  public static int getInboxMessages() throws IOException, GeneralSecurityException {
    return getMessagesForLabel(INBOX_ID);
  }


  public static void main(String[] args) throws Exception {
    Gmail service = buildClient();
    getMessagesForLabel(SENT_ID);
  }

}

