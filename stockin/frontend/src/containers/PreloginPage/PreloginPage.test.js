import React from 'react';
import {
  render,
  screen,
  fireEvent,
  queryAllByTestId,
  getByPlaceholderText,
} from '@testing-library/react';
import PreloginPage from './PreloginPage';
import { history } from '../../store/store';
import { Provider } from 'react-redux';
import { getMockStore } from '../../test-utils/mocks';
import * as authentication from '../../store/authentication/authentication';

jest.mock('../../components/Header/Header', () => {
  return jest.fn((props) => {
    return <div className="spyHeader"></div>;
  });
});

jest.mock('../../components/Footer/Footer', () => {
  return jest.fn((props) => {
    return <div className="spyFooter"></div>;
  });
});

const initialAuthState = { loggingIn: false, user: { id: 1 } };
const initialAuthStateLogin = { loggingIn: true, user: null };
const initialAuthStateUndefined = { loggingIn: undefined, user: null };
const mockStore = getMockStore(initialAuthState);
const mockStoreLogin = getMockStore(initialAuthStateLogin);
const mockStoreUndefined = getMockStore(initialAuthStateUndefined);

describe('<PreloginPage />', () => {
  let preLoginPage,
    preLoginPageLogin,
    preLoginPageUndefined,
    spyHistoryPush,
    spyTryLogin,
    spyCheckLogin;

  beforeEach(() => {
    preLoginPage = (
      <Provider store={mockStore}>
        <PreloginPage history={history} />
      </Provider>
    );

    preLoginPageLogin = (
      <Provider store={mockStoreLogin}>
        <PreloginPage history={history} />
      </Provider>
    );

    preLoginPageUndefined = (
      <Provider store={mockStoreUndefined}>
        <PreloginPage history={history} />
      </Provider>
    );

    spyHistoryPush = jest.spyOn(history, 'push').mockImplementation((text) => {
      return (dispatch) => {};
    });
    spyTryLogin = jest.spyOn(authentication, 'tryLogin').mockImplementation((user) => {
      return (dispatch) => {};
    });
    spyCheckLogin = jest.spyOn(authentication, 'checkLogin').mockImplementation(() => {
      return (dispatch) => {};
    });
  });

  it('should render without errors', () => {
    const { container } = render(preLoginPage);
    const query = queryAllByTestId(container, 'PreloginPage');
    expect(query.length).toBe(1);
  });

  test(`should change tab when 'About Stockin' clicked`, () => {
    const { container } = render(preLoginPage);
    fireEvent.click(screen.getByText(/about stockin/i));
    const query = queryAllByTestId(container, 'Stockin');
    expect(query.length).toBe(1);
  });

  test(`should change tab when 'About Us' clicked`, () => {
    const { container } = render(preLoginPage);
    fireEvent.click(screen.getByText(/about us/i));
    const query = queryAllByTestId(container, 'AboutUs');
    expect(query.length).toBe(1);
  });

  test(`should change tab when 'Preview' clicked`, () => {
    const { container } = render(preLoginPage);
    fireEvent.click(screen.getByText(/preview/i));
    const query = queryAllByTestId(container, 'Preview');
    expect(query.length).toBe(1);
  });

  test(`should change value in email input field`, () => {
    const { container } = render(preLoginPage);
    const query = getByPlaceholderText(container, 'Email');
    fireEvent.change(query, { target: { value: 'test@email.com' } });
    expect(query.value).toBe('test@email.com');
  });

  test(`should change value in password input field`, () => {
    const { container } = render(preLoginPage);
    const query = getByPlaceholderText(container, 'Password');
    fireEvent.change(query, { target: { value: 'password' } });
    expect(query.value).toBe('password');
  });

  test(`should dispatch tryLogin`, () => {
    const { container } = render(preLoginPage);
    const email = getByPlaceholderText(container, 'Email');
    fireEvent.change(email, { target: { value: 'test@email.com' } });
    const password = getByPlaceholderText(container, 'Password');
    fireEvent.change(password, { target: { value: 'password' } });
    fireEvent.click(screen.getByText(/Login/i, { selector: 'button' }));
    expect(spyTryLogin).toHaveBeenCalledTimes(1);
  });

  it('should redirect to when loggingIn = true', () => {
    render(preLoginPageLogin);
    expect(spyHistoryPush).toHaveBeenCalledTimes(1);
  });

  it('should dispatch checkLogin when loggingIn = undefined', () => {
    render(preLoginPageUndefined);
    expect(spyCheckLogin).toHaveBeenCalledTimes(1);
  });
});
